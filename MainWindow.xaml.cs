using System;
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
        string dataSet = "cards.txt";
        public MainWindow()
        {
            InitializeComponent();
            // Start the program with question already showing
            FlashCard randomVerb = GetFlashCard(); // Get our random verb
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
            FlashCard randomVerb = GetFlashCard();
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


        private FlashCard GetFlashCard()
        {
            StreamReader sr = new StreamReader(dataSet); // Createe a new stream reader
            List<FlashCard> cards = new List<FlashCard>(); //Create an empty list of Type FlashCard called cards
            string str = sr.ReadLine();
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
            Random randomNumber = new Random(); 
            int x = randomNumber.Next(cards.Count); // Creates a random number
            return cards[x]; // Returns a random flashcard
        }



        private void ShowWordsButton_Click(object sender, RoutedEventArgs e)
        {
            // Same as GetFlashCard this creates a list of whats in our text file. This time
            // however it is so we can show a list when clicking on the button.
            StreamReader sr = new StreamReader(dataSet);
            List<FlashCard> cards = new List<FlashCard>();
            string str = sr.ReadLine();
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

            StringBuilder builder = new StringBuilder(); // Create string builder
            int count = 0;
            foreach (var word in cards) // Loop through all strings
            {
                // This creates a very long string of all words in cards.txt and links questions
                // with answers and then puts each on a new line.
                builder.Append(cards[count].Question + " - " + cards[count].Answer).Append("\n"); 
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
            MessageBox.Show("Instructions:"
                + "\n\nWord Game:"
                + "\n\nThe aim of the word game is to match each of the english meanings to the Japanese word."
                + "\nYou can change the target score by changing the number at the top right of the screen and the targt score will be updated automatically."
                + "\nYou can find the words that are used for the word game by clicking the 'Verbs' button."
                + "\n\nConcepts:"
                + "\n\nHere you will find concepts such as particles (words used to mark the subject of a word), past and future tense and other concepts used within the language."
                + "\n\nExercises:"
                + "\n\nThe idea behind this section is for you to grab a pen and paper and complete the included exercises such as translating a small sentance from English to Japanese."
                +"",
                "Instructions");
        }

        private void ConceptsButton_Click(object sender, RoutedEventArgs e) // Shows concepts pop up
        {
            MessageBox.Show("Concepts:"
                + "\n\nWa - 'About' Marker"
                + "\nMarks the topic or subject of the sentence, as the word before it. Basically it describes what you are talking about."
                + "\n\nKa - '?' Verbal question marker"
                + "\nPlaced at the end of a sentence to indicate it is a quesiton"
                + "\n\nDa - 'is' Marker"
                + "\nPlaced at the end of a sentence to indicate what is being said 'is/am'"
                + "",
                "Concepts");
        }

        private void ExercisesButton_Click(object sender, RoutedEventArgs e) // Shows exercises popup
        {
            MessageBox.Show("Exercises:"
                + "\n\nFrom Japanese to English:"
                + "\n\nOre wa Wakaru"
                + "\nOre wa Shiru"
                + "\nOmae wa iu"
                + "\nShinobi wa wakaru ka"
                + "\nSore wa sato da",
                "Exercises");
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            dataSet = DataSetBox.Text + ".txt";
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
