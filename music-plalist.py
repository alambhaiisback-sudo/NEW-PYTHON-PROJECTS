songs = []

while True:
    print("\n--- MUSIC PLAYLIST ---")
    print("1. Add Song")
    print("2. Show Songs")
    print("3. Remove Song")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        song = input("Enter song name: ")
        songs.append(song)
        print("Song added!")

    elif choice == "2":
        if len(songs) == 0:
            print("Playlist is empty.")
        else:
            print("\nYour Songs:")
            for i, song in enumerate(songs, 1):
                print(i, ".", song)

    elif choice == "3":
        song = input("Enter song name to remove: ")

        if song in songs:
            songs.remove(song)
            print("Song removed!")
        else:
            print("Song not found.")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")