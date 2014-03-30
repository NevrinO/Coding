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
        private string dataSet = "cards.txt", instructions, concepts, exercises;
        private List<FlashCard> deck;
        public MainWindow()
        {
            InitializeComponent(); // Start the program with question already showing
            deck = loadFile();
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
            instructions = "";
            concepts = "";
            exercises = "";
            List<FlashCard> cards = new List<FlashCard>(); //Create an empty list of Type FlashCard called cards
            string str = sr.ReadLine();
            while (str != "-end-")
            {
                instructions += str + "\n";
                str = sr.ReadLine();
            }
            str = sr.ReadLine();
            while (str != "-end-")
            {
                concepts += str + "\n";
                str = sr.ReadLine();
            }
            str = sr.ReadLine();
            while (str != "-end-")
            {
                exercises += str + "\n";
                str = sr.ReadLine();
            }
            str = sr.ReadLine();
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
            return cards;
        }


        private void ShowWordsButton_Click(object sender, RoutedEventArgs e)
        {
            StringBuilder builder = new StringBuilder(); // Create string builder
            int count = 0;
            foreach (var word in deck) // Loop through all strings
            {
                // This creates a very long string of all words in cards.txt and links questions
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
            MessageBox.Show(instructions);
        }

        private void ConceptsButton_Click(object sender, RoutedEventArgs e) // Shows concepts pop up
        {
            MessageBox.Show(concepts);
        }

        private void ExercisesButton_Click(object sender, RoutedEventArgs e) // Shows exercises popup
        {
            MessageBox.Show(exercises);
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            dataSet = DataSetBox.Text + ".txt";
            deck = loadFile();
            Random randomNumber = new Random();
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
