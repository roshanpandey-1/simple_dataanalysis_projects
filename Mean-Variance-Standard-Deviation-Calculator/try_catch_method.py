import numpy as np

def calculate(data):
    try:
        if len(data) != 9:
            raise ValueError("List must contain nine numbers.")
        
        # Convert list into 3x3 numpy array
        matrix = np.array(data).reshape(3, 3)
        
        # Create a dictionary with all required statistics
        calculations = {
            'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()],
            'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()],
            'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()],
            'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()],
            'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()],
            'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]
        }
        
        return calculations
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
