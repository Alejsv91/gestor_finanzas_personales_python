def check_instance(value: any, expectedType: any, errorDescription: str)-> bool:  
        try:
            if not(isinstance(value, expectedType)):
                raise ValueError(errorDescription)
            
        except (ValueError, TypeError) as e:
            raise ValueError(f"System error when trying to save amount data. Error description: {e}")