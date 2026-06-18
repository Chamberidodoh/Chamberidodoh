def main():
    print("Hello from python-series!")


if __name__ == "__main__":
    main()


# This keeps running even if file doesn't exist
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("Could not find data.txt")
    content = "default data"
print("Done!")  # Always reaches here


try:
    # Code that might cause an error
    risky_operation()
except:
    # Code that runs if there's an error
    print("Something went wrong")



try:
    age = int(input("Enter your age: "))
    print(f"In 10 years, you'll be {age + 10}")
except ValueError:
    print("Please enter a number")



try:
    # Read a number from a file
    with open('number.txt', 'r') as f:
        text = f.read()
    number = int(text)
    result = 100 / number
    print(f"Result: {result}")
except FileNotFoundError:
    print("Could not find number.txt")
except ValueError:
    print("File doesn't contain a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")


try:
    with open('data.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
else:
    # This only runs if the file was opened successfully
    print(f"File has {len(data)} characters")


try:
    file = open('data.txt', 'r')
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    # This always runs to clean up
    if 'file' in locals() and not file.closed:
        file.close()
    print("Cleanup complete")



# Bad - catches everything
try:
    process_data()
except:
    pass  # Silent failure!

# Good - specific error
try:
    process_data()
except ValueError:
    print("Invalid data format")


# Bad - ignores the error
try:
    risky_operation()
except ValueError:
    pass

# Good - at least log it
try:
    risky_operation()
except ValueError:
    print("Warning: Invalid value encountered")


# Bad - hides all errors
try:
    critical_operation()
except Exception as e:
    print(f"Error: {e}")

# Good - log and re-raise
try:
    critical_operation()
except Exception as e:
    print(f"Critical error: {e}")
    raise  # Let the error propagate



import os

# Check first
if os.path.exists('data.txt'):
    with open('data.txt', 'r') as f:
        content = f.read()
else:
    print("File not found")

# Or use try-except
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    content = ""  # Default value


# Check if key exists
if "email" in user:
    print(user["email"])

# Use get() with default
email = user.get("email", "no-email@example.com")

# Or handle the error
try:
    print(user["email"])
except KeyError:
    print("Email not found")