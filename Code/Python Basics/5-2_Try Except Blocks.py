test_file = 'test_file.txt'
# test_file = 'testfile.txt'
status = None

# runs first and checks if error.
try:        
    open_file = open(test_file)
    status = "Success"
    # if test_file != "testfile.txt":
    #     raise Exception

# excepts catches errors.
except FileNotFoundError:
    print(f'ERROR: File does not exist. File name: {test_file}')
except Exception as error:
    print(f'ERROR: {error}')

# runs if no error found in try block.
else:
    print(f'FILE CONTENT: {open_file.read()}')
    open_file.close()

# runs regardless of error or not.
finally:
    status = "Fail" if status != "Success" else status
    print(f"MESSAGE: Executing finally block, end of the code. STATUS: {status}")