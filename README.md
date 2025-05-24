# VP
Virtual pet
At the beginning of the program, it will prompt the user to select the type of pet (such as dog, cat, pig, etc.), and then enter the name of the pet. The system creates a pet object based on the selection and outputs a welcome message.

Next, the program enters a loop, continuously allowing the user to interact with the pet until the pet dies or the user opts to exit. In each round of the loop, users can select different operations from the menu, including: feeding, playing, bathing, sleeping, administering medicine, checking the pet's status or quitting the game. Each operation will affect the attribute values of the pet, such as health, hunger, happiness, cleanliness and energy.

No matter which operation the user performs, the program will automatically carry out "attribute decay" at the end of that round, that is, hunger increases, happiness decreases, cleanliness decreases, and energy decreases. If the pet's condition deteriorates, such as hunger reaching 100, happiness being 0 or cleanliness being 0, its health value will decline. Once the health drops to 0, the pet will die and the game will end.

When a pet dies, the program will display a prompt message indicating that the pet has left. If the user manually exits, the current status of the pet will also be displayed and the game will end.
