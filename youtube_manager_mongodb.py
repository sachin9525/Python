import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from pymongo import MongoClient, PyMongoError

load_dotenv()

username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")
cluster = os.getenv("MONGODB_CLUSTER")
app_name = os.getenv("MONGODB_APP_NAME", "Cluster0")

if not username or not password or not cluster:
    raise RuntimeError(
        "Set MONGODB_USERNAME, MONGODB_PASSWORD, and MONGODB_CLUSTER in .env"
    )

encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

MONGO_URL = (
    f"mongodb+srv://{encoded_username}:{encoded_password}"
    f"@{cluster}/?appName={quote_plus(app_name)}"
)

try:
    client = MongoClient(
        MONGO_URL,
        serverSelectionTimeoutMS=5000
    )

    client.admin.command("ping")

    print("✅ MongoDB connected successfully!")

    db = client["youtube_manager"]
    video_collection = db["videos"]

except Exception as error:
    print("❌ MongoDB connection failed!")
    print(error)


# ==========================================
# Database and Collection
# ==========================================

db = client["youtube_manager"]

videos_collection = db["videos"]


# ==========================================
# 1. List All Videos
# ==========================================

def list_all_videos():

    print("\n" + "=" * 50)
    print("🎬 ALL VIDEOS")
    print("=" * 50)

    videos = list(videos_collection.find())

    if not videos:
        print("No videos found.")
        return

    for index, video in enumerate(videos, start=1):
        print(
            f"{index}. {video['name']} "
            f"| Duration: {video['time']}"
        )


# ==========================================
# 2. Add Video
# ==========================================

def add_video():

    print("\n➕ ADD VIDEO")

    name = input("Enter video name: ").strip()
    time = input("Enter video duration: ").strip()

    if not name or not time:
        print("❌ Name and duration are required.")
        return

    video = {
        "name": name,
        "time": time
    }

    result = videos_collection.insert_one(video)

    print("✅ Video added successfully!")
    print("MongoDB ID:", result.inserted_id)


# ==========================================
# 3. Update Video
# ==========================================

def update_video():

    print("\n✏️ UPDATE VIDEO")

    old_name = input(
        "Enter video name to update: "
    ).strip()

    video = videos_collection.find_one(
        {"name": old_name}
    )

    if not video:
        print("❌ Video not found.")
        return

    new_name = input(
        "Enter new video name: "
    ).strip()

    new_time = input(
        "Enter new duration: "
    ).strip()

    update_data = {}

    if new_name:
        update_data["name"] = new_name

    if new_time:
        update_data["time"] = new_time

    if not update_data:
        print("No changes provided.")
        return

    videos_collection.update_one(
        {"_id": video["_id"]},
        {
            "$set": update_data
        }
    )

    print("✅ Video updated successfully!")


# ==========================================
# 4. Delete Video
# ==========================================

def delete_video():

    print("\n🗑️ DELETE VIDEO")

    name = input(
        "Enter video name to delete: "
    ).strip()

    result = videos_collection.delete_one(
        {"name": name}
    )

    if result.deleted_count:
        print("✅ Video deleted successfully!")
    else:
        print("❌ Video not found.")


# ==========================================
# 5. Search Video
# ==========================================

def search_video():

    print("\n🔍 SEARCH VIDEO")

    name = input(
        "Enter video name to search: "
    ).strip()

    videos = videos_collection.find(
        {
            "name": {
                "$regex": name,
                "$options": "i"
            }
        }
    )

    videos = list(videos)

    if not videos:
        print("❌ No matching videos found.")
        return

    print("\nSearch Results:")

    for index, video in enumerate(videos, start=1):
        print(
            f"{index}. {video['name']} "
            f"| Duration: {video['time']}"
        )


# ==========================================
# Main Program
# ==========================================

def main():

    while True:

        print("\n" + "=" * 50)
        print("🎬 YOUTUBE MANAGER - MONGODB")
        print("=" * 50)

        print("1. List all videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Search video")
        print("6. Exit")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        try:

            if choice == "1":
                list_all_videos()

            elif choice == "2":
                add_video()

            elif choice == "3":
                update_video()

            elif choice == "4":
                delete_video()

            elif choice == "5":
                search_video()

            elif choice == "6":
                print(
                    "\n👋 Thanks for using "
                    "YouTube Manager!"
                )
                break

            else:
                print(
                    "❌ Invalid choice. "
                    "Please select 1-6."
                )

        except PyMongoError as error:
            print("❌ Database Error:", error)

        except Exception as error:
            print("❌ Error:", error)


# ==========================================
# Run Application
# ==========================================

if __name__ == "__main__":
    try:
        main()
    finally:
        client.close()