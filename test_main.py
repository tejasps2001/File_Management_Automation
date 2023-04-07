#! /usr/bin/env python3

import os
import main
import random
import unittest


class TestMain(unittest.TestCase):
    def test_wrong_filename(self):
        self.f1 = open("file 1.txt", "w")
        self.f2 = open("file abc.txt", "w")
        self.assertEqual(
            "file_1.txt",
            os.path.basename(main.convert_filename("file 1.txt", os.getcwd())),
        )
        self.assertEqual(
            "file_abc.txt",
            os.path.basename(main.convert_filename("file abc.txt", os.getcwd())),
        )
        self.f1.close()
        self.f2.close()
        os.remove(os.path.join(os.getcwd(), "file_1.txt"))
        os.remove(os.path.join(os.getcwd(), "file_abc.txt"))

    def test_logging(self):
        home_directory = os.path.expanduser("~")
        # Give a random number in the name to make the name unique everytime.
        # This will make it easy to test multiple times without changing name of file.
        self.f3 = open(
            "test_video" + str(random.choice(range(1000, 9999))) + ".mkv", "wb"
        )
        main.file_transfer(os.getcwd(), home_directory)
        with open(os.path.join(home_directory, "File-Transfer-Log.txt"), "r") as f:
            log_content = f.read()
        self.assertIn(
            "Moved " + self.f3.name + " to /home/top2001/Videos",
            log_content,
        )
        self.f3.close()
        os.remove(os.path.join(home_directory, "Videos", self.f3.name))


if __name__ == "__main__":
    unittest.main()
