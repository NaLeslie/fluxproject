import tkinter as tk

# -*- coding: utf-8 -*-
"""  
Flux: Source Code Vers. 1.0.2
Copyright (c) 2019 Lisa Stephens
With minor changes by Nathaniel Leslie (2020)

 This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

This script contains the source code for Flux, a GUI developed to simplify the
process of treating scanning electrochemical microscopy data sets. 

A separate class has been defined for each experiment type (image, CV, CA, 
approach curve) which consists of the set of functions required to process it. 
These classes have the following basic structure:
1. __init__ : Sets up the window, initializes a blank figure
2. SelectFile : Opens a file dialogue window to select a dataset
3. ImportFile : Based on the filetype/manufacturer, imports the dataset and 
   reshapes it into a consistent form for further analysis.
4. ReshapeData : Processes the data set based on the options selected by 
   the user. Updates the figure with the current processing settings.
5. BoxesSelected : Enables/disables functions in the GUI based on current 
   settings
6. SaveFig : Save figure to .png file
7. SaveTxt : Save processed data to .txt file
8. ResetWindow : Clear dataset, figure, and labels

Flux has been tested with the following package versions: numpy v1.16.2, 
pandas v0.24.1, scipy v1.2.1, scikit-image v0.14.2, matplotlib v3.0.3; some 
stability issues have been observed with other versions (particularly between 
numpy/scikit-image).


"""


class MenuPagesPAC:
    @staticmethod
    def TheoryPage(root):
        windowTheory = tk.Toplevel(root)
        windowTheory.title('Flux')  # window title
        windowTheory.wm_iconbitmap('supporting/flux_logo.ico')  # window icon

        frameTheory = tk.Frame(windowTheory)
        frameTheory.configure(background="white")
        frameTheory.pack(side="top")

        # Create text widget with scrollbar to contain large amounts of text
        scrollbarTheory = tk.Scrollbar(frameTheory)
        scrollbarTheory.pack(side="right", fill="y")

        textTheory = tk.Text(frameTheory, height=30, width=60, yscrollcommand=scrollbarTheory.set, borderwidth=0,
                             background="white", font='Arial 10')

        # Import external files/images which contain the contents of the help page
        try:
            # Part 0A: Normalization - text
            with open('supporting/text_PAC_general.txt', 'r') as fh:
                for line in fh:
                    textBlockTheory = fh.readline()
                    textTheory.insert("end", textBlockTheory)
                    textTheory.insert("end", "\n")
            fh.close()
            # Part 1B: Normalization - equation
            imageIss = tk.PhotoImage(file="supporting/eqn_steadystate.gif")
            textTheory.image_create("end", image=imageIss)
            textTheory.insert("end", "\n")

            # Part 1A: Normalization - text
            with open('supporting/text_CV_normalization.txt', 'r') as fh:
                for line in fh:
                    textBlockTheory = fh.readline()
                    textTheory.insert("end", textBlockTheory)
                    textTheory.insert("end", "\n")
            fh.close()
            # Part 1B: Normalization - equation
            imageIss = tk.PhotoImage(file="supporting/eqn_steadystate.gif")
            textTheory.image_create("end", image=imageIss)
            textTheory.insert("end", "\n")

            # Part 2A: Beta - text
            with open('supporting/text_CV_beta.txt', 'r') as fh:
                for line in fh:
                    textBlockTheory = fh.readline()
                    textTheory.insert("end", textBlockTheory)
                    textTheory.insert("end", "\n")
            fh.close()
            # Part 2B: Beta - equation
            imageBeta = tk.PhotoImage(file="supporting/eqn_beta.gif")
            textTheory.image_create("end", image=imageBeta)
            textTheory.insert("end", "\n")

            # Part 4A: Negfb - text
            with open('supporting/text_PAC_negfb.txt', 'r') as fh:
                for line in fh:
                    textBlockTheory = fh.readline()
                    textTheory.insert("end", textBlockTheory)
                    textTheory.insert("end", "\n")

            fh.close()

            # Part 3B: Negfb - equation
            imageNegfb = tk.PhotoImage(file="supporting/eqn_negfb.gif")
            textTheory.image_create("end", image=imageNegfb)
            textTheory.insert("end", "\n")

            # Part 4A: Posfb - text
            with open('supporting/text_PAC_posfb.txt', 'r') as fh:
                for line in fh:
                    textBlockTheory = fh.readline()
                    textTheory.insert("end", textBlockTheory)
                    textTheory.insert("end", "\n")

            fh.close()

            # Part 4B: Posfb - equation
            imagePosfb = tk.PhotoImage(file="supporting/eqn_posfb.gif")
            textTheory.image_create("end", image=imagePosfb)
            textTheory.insert("end", "\n")

            # Part 4C: Posfb (alpha) - equation
            imagePosfb2 = tk.PhotoImage(file="supporting/eqn_posfb_alpha.gif")
            textTheory.image_create("end", image=imagePosfb2)
            textTheory.insert("end", "\n")

            # Part 5A: Mixed fb - text
            with open('supporting/text_PAC_mixedfb.txt', 'r') as fh:
                for line in fh:
                    textBlockTheory = fh.readline()
                    textTheory.insert("end", textBlockTheory)
                    textTheory.insert("end", "\n")

            fh.close()

            # Part 5E: Mixed kinetics - equation
            imageMixedfb = tk.PhotoImage(file="supporting/eqn_mixedfb.gif")
            textTheory.image_create("end", image=imageMixedfb)
            textTheory.insert("end", "\n")

        except:
            print("Error importing help text.")

        textTheory.config(padx=20, pady=20, wrap="word")
        textTheory.pack()

        scrollbarTheory.config(command=textTheory.yview)

        windowTheory.mainloop()

    @staticmethod
    def GuidePage(root):
        windowGuide = tk.Toplevel(root)
        windowGuide.title('Flux')  # window title
        windowGuide.wm_iconbitmap('supporting/flux_logo.ico')  # window icon

        frameGuide = tk.Frame(windowGuide)
        frameGuide.configure(background="white")
        frameGuide.pack(side="top")

        # Create text widget with scrollbar to contain large amounts of text
        scrollbarGuide = tk.Scrollbar(frameGuide)
        scrollbarGuide.pack(side="right", fill="y")

        textGuide = tk.Text(frameGuide, height=30, width=40, yscrollcommand=scrollbarGuide.set, borderwidth=0,
                            background="white", font='Arial 10')

        # Import external files/images which contain the contents of the page
        try:
            with open('supporting/text_PAC_guide.txt', 'r') as fh:
                for line in fh:
                    textBlockGuide = fh.readline()
                    textGuide.insert("end", textBlockGuide)
                    textGuide.insert("end", "\n")
            fh.close()

        except:
            print("Error importing help text.")

        textGuide.config(padx=20, pady=20, wrap="word")
        textGuide.pack()

        scrollbarGuide.config(command=textGuide.yview)

        windowGuide.mainloop()

    @staticmethod
    def AboutPage(root, version):
        windowAbout = tk.Toplevel(root)
        windowAbout.title('Flux')
        windowAbout.wm_iconbitmap('supporting/flux_logo.ico')  # window icon

        frameLogo = tk.Frame(windowAbout)
        frameLogo.pack(side="left")
        frameAbout = tk.Frame(windowAbout)
        frameAbout.pack(side="right")

        imageLogo = tk.PhotoImage(file="supporting/flux_logo_large.gif")
        labelLogo = tk.Label(frameLogo, image=imageLogo)
        labelLogo.grid(row=0, column=0, padx=30, pady=30)

        labelAbout = tk.Label(frameAbout, text=version, font=36)
        labelAbout.grid(row=0, column=0, sticky="W" + "N", pady=10)
        labelAbout = tk.Label(frameAbout, text="GUI for treating SECM data\n Licensed under GNU GPL v3")
        labelAbout.grid(row=1, column=0, sticky="W" + "N", padx=10)

        windowAbout.mainloop()
