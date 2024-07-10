def create_dict(i, j, default_value=0):
    return {key: default_value for key in range(i, j + 1)}

lines = ['ge', 'da', 'gert', 'tgreger']
# Example usage
i = 1
j = 5
result_dict = create_dict(i, j)

print(result_dict)


scans = {key: [] for key in range(1, len(lines)+1)}
print(scans)