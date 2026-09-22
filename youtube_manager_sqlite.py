import sqlite3

DATABASE_NAME = "youtube_videos.db"


# ==========================================
# Database Connection
# ==========================================

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()


# ==========================================
# Create Videos Table
# ==========================================

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )
    """)

    conn.commit()


# ==========================================
# List All Videos
# ==========================================

def list_all_videos():

    cursor.execute("SELECT * FROM videos")

    videos = cursor.fetchall()

    print("\n" + "*" * 50)
    print("🎬 ALL YOUTUBE VIDEOS")
    print("*" * 50)

    if not videos:
        print("No videos found.")
        return

    for video in videos:

        print(
            f"ID: {video[0]} | "
            f"Name: {video[1]} | "
            f"Duration: {video[2]}"
        )


# ==========================================
# Add Video
# ==========================================

def add_video():

    print("\n--- Add New Video ---")

    name = input("Enter video name: ").strip()
    time = input("Enter video duration: ").strip()

    if not name or not time:
        print("❌ Name and duration cannot be empty.")
        return

    cursor.execute(
        """
        INSERT INTO videos (name, time)
        VALUES (?, ?)
        """,
        (name, time)
    )

    conn.commit()

    print("✅ Video added successfully!")


# ==========================================
# Update Video
# ==========================================

def update_video():

    list_all_videos()

    try:

        video_id = int(
            input("\nEnter video ID to update: ")
        )

        cursor.execute(
            "SELECT * FROM videos WHERE id = ?",
            (video_id,)
        )

        video = cursor.fetchone()

        if video is None:
            print("❌ Video not found.")
            return

        print("\nCurrent Video:")
        print("Name:", video[1])
        print("Duration:", video[2])

        name = input("Enter new video name: ").strip()
        time = input("Enter new duration: ").strip()

        cursor.execute(
            """
            UPDATE videos
            SET name = ?, time = ?
            WHERE id = ?
            """,
            (name, time, video_id)
        )

        conn.commit()

        print("✅ Video updated successfully!")

    except ValueError:

        print("❌ Please enter a valid ID.")


# ==========================================
# Delete Video
# ==========================================

def delete_video():

    list_all_videos()

    try:

        video_id = int(
            input("\nEnter video ID to delete: ")
        )

        cursor.execute(
            "SELECT * FROM videos WHERE id = ?",
            (video_id,)
        )

        video = cursor.fetchone()

        if video is None:
            print("❌ Video not found.")
            return

        cursor.execute(
            "DELETE FROM videos WHERE id = ?",
            (video_id,)
        )

        conn.commit()

        print(
            f"✅ '{video[1]}' deleted successfully!"
        )

    except ValueError:

        print("❌ Please enter a valid ID.")


# ==========================================
# Search Video
# ==========================================

def search_video():

    name = input(
        "\nEnter video name to search: "
    ).strip()

    cursor.execute(
        """
        SELECT * FROM videos
        WHERE name LIKE ?
        """,
        (f"%{name}%",)
    )

    videos = cursor.fetchall()

    if not videos:

        print("❌ No matching videos found.")
        return

    print("\n🔍 SEARCH RESULTS")
    print("-" * 50)

    for video in videos:

        print(
            f"ID: {video[0]} | "
            f"Name: {video[1]} | "
            f"Duration: {video[2]}"
        )


# ==========================================
# Main Program
# ==========================================

def main():

    # IMPORTANT:
    # Table is created before menu starts
    create_table()

    while True:

        print("\n" + "=" * 45)
        print("🎬 YOUTUBE MANAGER - SQLITE3")
        print("=" * 45)

        print("1. List all videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Search video")
        print("6. Exit")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        match choice:

            case "1":
                list_all_videos()

            case "2":
                add_video()

            case "3":
                update_video()

            case "4":
                delete_video()

            case "5":
                search_video()

            case "6":
                print(
                    "\n👋 Thanks for using "
                    "YouTube Manager!"
                )
                break

            case _:
                print(
                    "❌ Invalid choice. "
                    "Please select 1-6."
                )


# ==========================================
# Start Application
# ==========================================

if __name__ == "__main__":

    try:

        main()

    except sqlite3.Error as error:

        print(
            "❌ SQLite Error:",
            error
        )

    finally:

        conn.close()

        print("🔒 Database connection closed.")