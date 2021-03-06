﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.IO; 

namespace JTALesson1
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private string dataSet = "cards.txt", instructions, concepts, exercises;
        private List<FlashCard> deck;
        public MainWindow()
        {
            InitializeComponent(); // Start the program with question already showing
            deck = loadFile(); // runs function and saves the returned list as deck.
            Random randomNumber = new Random(); 
            int x = randomNumber.Next(deck.Count); // Creates a random number
            FlashCard randomVerb = deck[x]; // Get our random verb
            MeaningBlock.Text = randomVerb.Question; // Send our random verb meaning to textblock
            JVerbBlock.Text = randomVerb.Answer; // Set Japanese verb to a hidden block to pass data to buttoon
            int score = 0;
            ScoreBlock.Text = score.ToString(); // Show score at 0 at start up
        }

        private void GetVerbButton_Click(object sender, RoutedEventArgs e)
        {
            string maxScoreText = MaxScoreBox.Text;
            int maxScore = Int32.Parse(maxScoreText);
            int score = Int16.Parse(ScoreBlock.Text);
            
            if (AnswerBox.Text == JVerbBlock.Text)
            {
                Console.ForegroundColor = ConsoleColor.Green;
                OutcomeBlock.Text = "Correct! The Answer Was: " + JVerbBlock.Text;
                score++;
                ScoreBlock.Text = score.ToString();
            }
            else
            {
                OutcomeBlock.Text = "Wrong! The Answer Was: " + JVerbBlock.Text;
            }
            Random randomNumber = new Random();
            int x = randomNumber.Next(deck.Count); // Creates a random number
            FlashCard randomVerb = deck[x]; // Get our random verb
            MeaningBlock.Text = randomVerb.Question;
            JVerbBlock.Text = randomVerb.Answer;
            AnswerBox.Clear();
            if (score >= maxScore)
            {
                MessageBox.Show("Congratulations! You reached your target score!",
                "Congratulation!");
                ScoreBlock.Text = "0";
            }
  
        }

        private List<FlashCard> loadFile()
        {
            StreamReader sr = new StreamReader(dataSet);
            instructions = ""; //Set variable to blank so when switching data sets it doesnt just add on to what was already there.
            concepts = ""; // same as above, you should try and remove these 3 lines just to see.
            exercises = ""; // same as above.
            List<FlashCard> cards = new List<FlashCard>(); //Create an empty list of Type FlashCard called cards
            string str = sr.ReadLine(); // reads in the next (or first in this case) line from the stream reader sr.
            while (str != "-end-") //this while statement adds everything before the first '-end-' to the string instructions
            {
                instructions += str + "\n";
                str = sr.ReadLine();
            }
            str = sr.ReadLine(); // this clears the '-end-' from str, without this it will skip the next while loop.
            while (str != "-end-") // this loop adds everything between the first and second '-end-' to the concepts string.
            {
                concepts += str + "\n";
                str = sr.ReadLine();
            }
            str = sr.ReadLine(); // this clears the '-end-' from str, without this it will skip the next while loop.
            while (str != "-end-") // this loop adds everything between the second and last '-end-' to the exercises string.
            {
                exercises += str + "\n";
                str = sr.ReadLine();
            }
            str = sr.ReadLine();// this clears the '-end-' from str, without this it will add '-end-' as the first question and all your questions and answers will be off.
            while (str != null)
            {
                FlashCard card = new FlashCard();  // create an empty Flashcard
                card.Question = str;  // set the Question to the first line read
                str = sr.ReadLine();  // read another line
                card.Answer = str;    // set the answer to the second line read
                cards.Add(card);      // add this flashcard to our collection
                str = sr.ReadLine();  // read the next line to see if there is more
            }
            sr.Close();  // we don't need the file open anymore
            return cards; // returns the list cards.
        }


        private void ShowWordsButton_Click(object sender, RoutedEventArgs e)
        {
            StringBuilder builder = new StringBuilder(); // Create string builder
            int count = 0;
            foreach (var word in deck) // Loop through all cards in deck
            {
                // This creates a very long string of all words in list deck and links questions
                // with answers and then puts each on a new line.
                builder.Append(deck[count].Question + " - " + deck[count].Answer).Append("\n"); 
                count++;
            }
            string result = builder.ToString(); // Get string from StringBuilder
            Console.WriteLine(result);

            MessageBox.Show("Verbs: \n\n" // Shows the list of words in a pop up box
                + result
                + ""
                ,
                "Verbs - Do Not Cheat ;)");
           
        }

        private void ResetScoreButton_Click(object sender, RoutedEventArgs e) // Reset Score
        {
            int score = 0;
            ScoreBlock.Text = score.ToString();
        }

        private void AboutButton_Click(object sender, RoutedEventArgs e) // Shows about popup
        {
            MessageBox.Show("Learning Japanese Demo 0.2 alpha"
                + "\n\nCoded by Dosk3n (Twitter @Dosk3n)"
                + "\n\nThanks go out to Joe Maruschek for his code suggestion",
                "About");
        }

        private void InstructionsButton_Click(object sender, RoutedEventArgs e) // Shows instructions popup
        {
            MessageBox.Show(instructions); // shows string.
        }

        private void ConceptsButton_Click(object sender, RoutedEventArgs e) // Shows concepts pop up
        {
            MessageBox.Show(concepts); // shows string.
        }

        private void ExercisesButton_Click(object sender, RoutedEventArgs e) // Shows exercises popup
        {
            MessageBox.Show(exercises); // shows string.
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            dataSet = DataSetBox.Text + ".txt";
            deck = loadFile(); // runs function and saves the returned list as deck.
            Random randomNumber = new Random(); // creates a new seed for rng.
            int x = randomNumber.Next(deck.Count); // Creates a random number
            FlashCard randomVerb = deck[x]; // Get our random verb
            MeaningBlock.Text = randomVerb.Question; // Send our random verb meaning to textblock
            JVerbBlock.Text = randomVerb.Answer; // Set Japanese verb to a hidden block to pass data to buttoon
            int score = 0;
            ScoreBlock.Text = score.ToString(); // Show score at 0 at start up
        }
    }

 

    class FlashCard
    {
        public string Question;
        public string Answer;

        // This is a default constructor that puts in some
        // defaults when the object is created.
        public FlashCard()
        {
            Question = "Unknown";
            Answer = "Unknown";
        }
    }
}
