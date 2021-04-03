# custom-object-help
Custom object and item help text files for Principia, intended to be bundled with 1.5.1.1.

## Installing
A Github action has been set up that combines the text files on each new commit. To download the latest commit, go to the **Actions** page for this repository, select the newest workflow run and download the `combined-help-files` artifact. It is an archive containing two files, `object_help.txt` and `item_help.txt`.
- For Windows, simply move these files into `data-shared/lang/en/`, replacing the old help files.
- For Android, you will need to make your own modded APK which replaces these files in the `assets/data-shared/lang/en/` folder inside of the APK.

## Contributing
Simply fork this repository, edit the object help files (the web editor works perfectly fine), and send a pull request.

Keep these things in mind when contributing:
- The text files do support a limited subset of HTML tags (mostly basic formatting such as bold, italics and underline), but if you use a tag it doesn't support it will throw out the entire object help file. Be careful!
- Newlines are preserved in the object help dialog, so you do not need `<br>` or `<p></p>` tags.

## License
The help text itself in this repository is licensed under CC0-1.0 due to the fact the original help files were put on the original Principia wiki under the Public Domain.

`combine.py` and `split.py` are licensed under the MIT license.
