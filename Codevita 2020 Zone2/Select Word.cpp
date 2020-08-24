#include <stdio.h>

#include <math.h>

#include <conio.h>

#include <process.h>

#include <string.h>

 

int ReadLine(FILE *fp, char *data, int len)

{

    int index = 0;

    while(1)

    {

        char ch;

        if( feof(fp))

            break;

        if( fread(&ch, 1, 1, fp) < 1)

            break;

 

        if(ch == '\n')

        {

            data[index++] = '\0';

            break;

        }

        data[index++] = ch;

    }

    return index;

}

 

 

int ReadWordsFromFile(char **p)

{

    int count = 0;

    char buf[128];

    FILE *istream = fopen("words_input.txt", "r");

    if (istream == 0)

        return -1;

 

    while(1)

    {

        if( feof(istream))

            break;

        if(ReadLine(istream, buf, 128) < 0)

            break;

        p[count] = (char*) malloc(128);

        strcpy(p[count], buf);

        count++;

    }

    fclose(istream);

    return count;

}

 

void main()

{

    int count = 0;

    char *words[100];

    char *secretWord;

    int guessX;

    int numChars = -1;

    int i, j;

    int bGuessedCorrectly = 0;

 

    printf("\nWelcome to Guess a Word\n");

    count = ReadWordsFromFile(words);

    if (count <= 0)

    {

          printf("\nNo words found in the file");

          return;

    }

    guessX = rand() % count;

    secretWord = words[guessX];

 

    numChars = strlen(secretWord);

 

    printf("Your secret word is: ");

    for(i = 0; i < numChars; i++)

          printf("*");

    printf("\n");

 

    printf("\nGuess now  (To stop the program, enter #) : ");

 

    while (1)

    {

          char choice[128];

        scanf("%s", choice);

 

          if (choice[0] == '#')

                break;

          if (strcmp(secretWord, choice) == 0)

          {

                bGuessedCorrectly = 1;

                break;

          }

          for (i = 0; i < numChars; i++)

          {

                if (i < strlen(secretWord) &&

                      i < strlen(choice))

                {

                      if (secretWord[i] == choice[i])

                            printf("%c", choice[i]);

                      else

                            printf("*");

                }

                else

                      printf("*");

          }

          printf("\n");

 

    }

    if (bGuessedCorrectly == 0)

          printf("\nUnfortunately you did not guess it correctly. The secret word is: %s", secretWord);

    else

          printf("\nCongrats! You have guessed it correctly");

 

    for(i = 0; i < count; i++)

        free(words[i]);

}
