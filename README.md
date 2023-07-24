# 🎉📂 Towel Zip Splitter! 📂🎉

ZipSplit is your handy companion to split those bulky ZIP files into bite-sized pieces and, it can also bring them back together! 

## 📚 What it Does 📚

ZipSplit uses the power of Python to give you an easy-to-use graphical interface to split large ZIP files into smaller parts. You can also merge these parts back into a single ZIP file! 💪 The size of the parts? You get to decide that! 🎛️

## 🚀 How to Get Started 🚀

### 🏗️ Building Standalone Executable/App 🏗️

We've got you covered whether you're on macOS or Windows! Just follow these steps:

#### 🍎 macOS:

1. Install PyInstaller if you haven't already (you only need to do this once!):

    ```shell
    pip install pyinstaller
    ```

2. Change directory to where your `ZipSplit.py` script lives:

    ```shell
    cd /path/to/your/ZipSplit.py
    ```

3. Let's build the application:

    ```shell
    pyinstaller --windowed --onefile --name ZipSplitter ZipSplit.py
    ```

4. Done! 🎉 You can find your shiny new app in the "dist" directory as "ZipSplitter.app". Time to make some ZIP magic! 

*Note: macOS app needs to be built on a macOS machine.*

#### 💻 Windows:

1. Make sure Python is installed. If not, you can get it from the official Python website.

2. Install PyInstaller if you haven't already (you only need to do this once!):

    ```shell
    pip install pyinstaller
    ```

3. Change directory to where your `ZipSplit.py` script lives:

    ```shell
    cd \path\to\your\ZipSplit.py
    ```

4. Let's build the executable:

    ```shell
    pyinstaller --onefile --windowed --name ZipSplitter ZipSplit.py
    ```

5. Voila! 🎉 Your "ZipSplitter.exe" is ready in the "dist" directory. Let's get zipping!

*Note: Windows .exe needs to be built on a Windows machine.*

### 🚀 How to Use ZipSplitter 🚀

After running `ZipSplit.py` or your shiny new app/executable:

To split a ZIP file:
1. Click "Split a ZIP file". 👈
2. Select the ZIP file you want to split. 🗂️
3. Decide how big you want the parts to be (in MB). 🎚️
4. Click "Split". 🎯

To merge ZIP parts:
1. Click "Merge ZIP parts". 👈
2. Select any part of the ZIP file. 🗂️
3. Click "Merge". 🎯

Congratulations, you're now a ZipSplitter pro! 💯
