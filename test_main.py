#! /usr/bin/env python3

import os
import main
import random
import unittest


class TestMain(unittest.TestCase):
    def test_wrong_filename(self):
        self.f1 = open("file 1.txt", "w")
        self.f2 = open("file abc.txt", "w")
        # Store the name and close the file objects because Windows can't access the files otherwise.
        self.f1.close()
        self.f2.close()
        self.assertEqual(
            "file_1.txt",
            os.path.basename(main.convert_filename("file 1.txt", os.getcwd())),
        )
        self.assertEqual(
            "file_abc.txt",
            os.path.basename(main.convert_filename(
                "file abc.txt", os.getcwd())),
        )
        os.remove(os.path.join(os.getcwd(), "file_1.txt"))
        os.remove(os.path.join(os.getcwd(), "file_abc.txt"))

    def test_logging(self):
        home_directory = os.path.expanduser("~")
        # Give a random number in the name to make the name unique everytime.
        # This will make it easy to test multiple times without changing name of file.
        self.f3 = open(
            "test_video" + str(random.choice(range(1000, 9999))) + ".mkv", "wb"
        )
        # Store the name and close the file objects because Windows can't access the files otherwise.
        video = self.f3.name
        self.f3.close()
        main.file_transfer(os.getcwd(), home_directory)
        with open(os.path.join(home_directory, "File-Transfer-Log.txt"), "r") as f:
            log_content = f.read()
        self.assertIn(
            "Moved " + video + " to " + os.path.join(home_directory, "Videos"),
            log_content,
        )
        os.remove(os.path.join(home_directory, "Videos", video))

    def test_transfer(self):
        home_directory = os.path.expanduser("~")
        # Test one file type from each category.
        # Give a random number in the name of the file to make it unique everytime.
        # This will make it easy to verify that the transfer worked.
        self.video = open(
            "test_video" + str(random.choice(range(1000, 9999))) + ".mkv", "wb"
        )
        self.music = open(
            "test_music" + str(random.choice(range(1000, 9999))) + ".mp3", "wb"
        )
        self.picture = open(
            "test_picture" +
            str(random.choice(range(1000, 9999))) + ".jpg", "wb"
        )
        self.doc = open(
            "test_doc" + str(random.choice(range(1000, 9999))) + ".xlsx", "wb"
        )
<<<<<<< HEAD
        # Store the name and close the file objects because Windows can't access the files otherwise.
        video = self.video.name
        music = self.music.name
        picture = self.picture.name
        doc = self.doc.name
=======
        main.file_transfer(os.getcwd(), home_directory)
        # Verify file transfers.
        self.assertIn(
            self.video.name, os.listdir(os.path.join(home_directory, "Videos"))
        )
        self.assertIn(
            self.music.name, os.listdir(os.path.join(home_directory, "Music"))
        )
        self.assertIn(
            self.picture.name, os.listdir(
                os.path.join(home_directory, "Pictures"))
        )
        self.assertIn(
            self.doc.name, os.listdir(
                os.path.join(home_directory, "Documents"))
        )
        # Close file objects and delete files.
>>>>>>> 4df588d (Auto-formatted code)
        self.video.close()
        self.music.close()
        self.picture.close()
        self.doc.close()
        main.file_transfer(os.getcwd(), home_directory)
        # Verify file transfers.
        self.assertIn(
            video, os.listdir(os.path.join(home_directory, "Videos"))
        )
        self.assertIn(
            music, os.listdir(os.path.join(home_directory, "Music"))
        )
        self.assertIn(
            picture, os.listdir(os.path.join(home_directory, "Pictures"))
        )
        self.assertIn(
            doc, os.listdir(os.path.join(home_directory, "Documents"))
        )
        # Close file objects and delete files.
        os.remove(os.path.join(home_directory, "Videos", video))
        os.remove(os.path.join(home_directory, "Music", music))
        os.remove(os.path.join(home_directory, "Pictures", picture))
        os.remove(os.path.join(home_directory, "Documents", doc))


if __name__ == "__main__":
    unittest.main()
