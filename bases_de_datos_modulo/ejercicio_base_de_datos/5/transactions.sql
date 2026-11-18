SET search_path TO store_db;

DO $$
DECLARE
    v_items JSONB := '[
        {"product_id": 1, "quantity": 2},
        {"product_id": 2, "quantity": 5}
    ]';
    v_item RECORD; 
    v_stock INT;
    v_product_price DECIMAL(10,2);
    v_user_id INT := 1;
    v_user_exist INT;
    v_bill_id INT;
    v_bill_product_id_temp INT;
    v_bill_product_ids INT[] := '{}'; 
    v_total DECIMAL(10,2) := 0; 
BEGIN
    -- 1. Confirmar que el usuario que realiza la compra existe en la DB
    SELECT COUNT(id) INTO v_user_exist
    FROM users
    WHERE id = v_user_id;

    IF v_user_exist = 0 THEN
        RAISE EXCEPTION 'El id del usuario % no existe.', v_user_id;
    END IF;
    
    -- 2. Insertar la factura con el usuario relacionado (total inicial en 0)
    INSERT INTO bills (date, user_id, total)
    VALUES (NOW(), v_user_id, 0)
    RETURNING id INTO v_bill_id;

    -- 3. Recorrer productos, validar stock, insertar detalle y restar inventario
    FOR v_item IN SELECT * FROM jsonb_to_recordset(v_items) AS x(product_id INT, quantity INT) LOOP
        
        SELECT stock, price INTO v_stock, v_product_price
        FROM products 
        WHERE id = v_item.product_id
        FOR UPDATE;

        IF v_stock IS NULL THEN
            RAISE EXCEPTION 'El producto ID % no existe.', v_item.product_id;
        ELSIF v_stock < v_item.quantity THEN
            RAISE EXCEPTION 'Stock insuficiente para producto %. Disponible: %, Solicitado: %', 
                            v_item.product_id, v_stock, v_item.quantity;
        END IF;

        -- Agregar la relación entre product y bill
        INSERT INTO product_bill (product_id, quantity, bill_id, unit_price)
        VALUES (v_item.product_id, v_item.quantity, v_bill_id, v_product_price)
        RETURNING id INTO v_bill_product_id_temp;

        -- Guardar el ID generado en el arreglo
        v_bill_product_ids := array_append(v_bill_product_ids, v_bill_product_id_temp);

        -- Reducir el stock del producto según la cantidad comprada
        UPDATE products
        SET stock = stock - v_item.quantity
        WHERE id = v_item.product_id;

        -- Sumar al total (cantidad * precio)
        v_total := v_total + (v_item.quantity * v_product_price);

        RAISE NOTICE 'Producto % OK (Cantidad: %)', v_item.product_id, v_item.quantity;
    END LOOP;

    -- 4. Actualizar el total calculado en la factura
    UPDATE bills
    SET total = v_total
    WHERE id = v_bill_id;

    RAISE NOTICE 'Factura % creada con éxito. Total: %. IDs detalle: %', v_bill_id, v_total, v_bill_product_ids;
END $$;
