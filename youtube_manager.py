import json

FILE_NAME = "youtube.txt"


# Load data from file
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


# Save data into file
def save_data(videos):
    with open(FILE_NAME, "w") as file:
        json.dump(videos, file, indent=4)


# List all videos
def list_all_videos(videos):
    print("\n" + "*" * 50)

    if not videos:
        print("No videos found.")
        print("*" * 50)
        return

    for index, video in enumerate(videos, start=1):
        print(
            f"{index}. {video['name']} "
            f"| Duration: {video['time']}"
        )

    print("*" * 50)


# Add new video
def add_video(videos):
    print("\n--- Add Video ---")

    name = input("Enter video name: ")
    time = input("Enter video duration: ")

    videos.append({
        "name": name,
        "time": time
    })

    save_data(videos)

    print("✅ Video added successfully!")


# Update video
def update_video(videos):
    list_all_videos(videos)

    if not videos:
        return

    try:
        index = int(
            input("Enter video number to update: ")
        )

        if 1 <= index <= len(videos):

            name = input("Enter new video name: ")
            time = input("Enter new duration: ")

            videos[index - 1]["name"] = name
            videos[index - 1]["time"] = time

            save_data(videos)

            print("✅ Video updated successfully!")

        else:
            print("❌ Invalid video number.")

    except ValueError:
        print("❌ Please enter a valid number.")


# Delete video
def delete_video(videos):
    list_all_videos(videos)

    if not videos:
        return

    try:
        index = int(
            input("Enter video number to delete: ")
        )

        if 1 <= index <= len(videos):

            deleted_video = videos.pop(index - 1)

            save_data(videos)

            print(
                f"✅ '{deleted_video['name']}' "
                "deleted successfully!"
            )

        else:
            print("❌ Invalid video number.")

    except ValueError:
        print("❌ Please enter a valid number.")


# Main Program
def main():

    videos = load_data()

    while True:

        print("\n" + "=" * 45)
        print("🎬 YOUTUBE MANAGER APP")
        print("=" * 45)

        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        match choice:

            case "1":
                list_all_videos(videos)

            case "2":
                add_video(videos)

            case "3":
                update_video(videos)

            case "4":
                delete_video(videos)

            case "5":
                print("\n👋 Thanks for using YouTube Manager!")
                break

            case _:
                print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()