SET search_path TO store_db;

DO $$
DECLARE
    v_return_bill INT := 5;
    v_bill_status VARCHAR(20);
    v_row RECORD;
BEGIN
    -- 1. Validar que la factura existe y traer su estado en una sola consulta
    SELECT status INTO v_bill_status
    FROM bills
    WHERE id = v_return_bill
    FOR UPDATE;

    IF v_bill_status IS NULL THEN
        RAISE EXCEPTION 'El id % no existe en bills', v_return_bill;
    ELSIF v_bill_status = 'RETURNED' THEN
        RAISE EXCEPTION 'La factura % no es una factura activa', v_return_bill;
    END IF;

    -- 2. Obtener los productos de la factura y devolver el stock
    FOR v_row IN
        SELECT * 
        FROM product_bill
        WHERE bill_id = v_return_bill
    LOOP
        RAISE NOTICE 'Product id: %, Quantity: %', v_row.product_id, v_row.quantity;

        -- Actualizar el stock
        UPDATE products
        SET stock = stock + v_row.quantity
        WHERE id = v_row.product_id;
    END LOOP;

    -- 3. Actualizar el bill a 'RETURNED'
    UPDATE bills
    SET status = 'RETURNED'
    WHERE id = v_return_bill;

    RAISE NOTICE 'Factura % marcada como RETURNED con éxito.', v_return_bill;
END $$;
