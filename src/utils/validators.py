def checkInstance(value: any, expectedType: any, errorDescription: str)-> bool:  
        try:
            if not(isinstance(value, expectedType)):
                raise ValueError(errorDescription)
            
        except (ValueError, TypeError) as e:
            raise SystemError(f"System error when trying to save amount data. Error description: {e}")