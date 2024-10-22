summary of password generator code:

### Password Generator in Python

This Python script generates a random password based on user preferences. It uses the `random` and `string` modules to create a password that includes different types of characters (lowercase letters, uppercase letters, digits, and symbols) based on user input.

**Features:**
- **Length**: User specifies the desired length of the password.
- **Character Types**: Users choose whether to include lowercase letters, uppercase letters, digits, and symbols.
- **Randomness**: The password is generated by randomly selecting characters from the chosen categories.

**Steps:**
1. **Input Collection**: Prompts the user to specify the length of the password and whether to include each type of character.
2. **Character Selection**: Based on the user's input, it creates a pool of characters from which the password will be generated.
3. **Password Generation**: Randomly selects characters from the pool and concatenates them to form the final password.
4. **Output**: Prints the generated password.

**Usage Example:**
- Input: `Length = 12`, `Include lowercase = yes`, `Include uppercase = yes`, `Include digits = yes`, `Include symbols = no`
- Output: A 12-character password containing lowercase letters, uppercase letters, and digits.

**Note:** If no character type is selected, the script prints "Invalid Input."
