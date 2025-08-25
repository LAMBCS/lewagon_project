# lewagon_project

This is a project to predict the EUR interest rate yield curve for the next n days where n could be say 5 up to 30 days based on previous yield curves.

The choice of n days is made to ensure that the prdeiction will go wildly wrong and that we should have significant differences in the metrics ensuring that we can compare how well the model behaves compared to the naive prediction which in this cae would be the current yield curve.

It imagines a world where an individual can only invest in government bonds, FTSE 100 stocks and gold.  I have all this data from about 2004 to 2025.  Some 5190 different dates.

The additional knowlege is the current, and previous, base rates and the last, and previously, published inflation rate.

The project is not really about forecasting the yield curve.  If we manage it in any meanigful sense we can all retire.

What the project is designed to do is cover as much of the syllabus as possible.

It is structured around developing a series of models of increasing complexity until we run out of time and then moving on with what we have to delivery.

I imagine the model trajectory to go something like:

I would be hopeful that we would do things faster than this timetable but by the end of day 1 we should have something to put into the production pahse even if it is awful.

DAY 1,

1. Base model. the yield curve today.
2. Simple regression model. (I am imaginig a sequence of linear regression models into the future)

DAY 2.

3. Moving onto a GRU structure chopping the data up into say the last 90 days.
4. using a convolution neural network to guess pictures of yield curves based off a previous sequence.  I have started creating photos of
   them using matplotlib.  If the data isn't ready we wouldn't do it.


DAY 3.

5. Ensemble methods putting the pictorial data and the numerical data together.  Ideally in a feedback loop where the prediction at t+1 is
   based off the prediction at t.
6. Text data to create a sentiment status (UP, Down, no-change) from textual data.  Using something like small bert and a free model.  I am
   collecting the data but whilst the documents are big I think this will be a wash as a predictor.  I would baseline this by simply making a judgement as I input the documents.  The source would be the IMF and ECB overviews.

Where I am with the data.

I have all the numneric data.

1. I have prepared the gold price data using date as an index and stored it as a .csv. (I prepared a DataFrame and then stored it)
2. I have prepared the yield curve formula coefficients in a .csv with date as an index. (I prepared the DataFrame and then stored it)
3. I have the excahnge rates in a .csv
4. I have the FSTE 100 index in a .csv.

Things to do

1. I need to convert the gold price into EUR for USD. (I have the exchange rate data as a .csv)
2. I need to generate the .PNG files of the yield curve from the yield curve data.  I am proposing to use Matplotlib to do this.
3. I need to put all the data into one DataFrame.
4. I need to store all the seperate tables in an SQL data base as well as .csv.


Padding an data dropping.

We are limited by the yield curve data.  We have something like 5000 data points.  They only exist for trading days which menas we will not have data for Sat, Sun and bank holidays.  We will not have to drop it, it will just not be there.

To the extent that other data is missing I will pad using the previous days data.  If it happens at all it will be because there is a difference in US holidays (gold price) and European ones.

Indexing.

I propose to eventually use a numeric index.  Hopefully we will be running up and down the DataFrame getting different sequences and also pulling different parts of the DataFrame and I believe that numerical calculations on the index will be easier than date.

Normalisation.

I believe we are going to need dynamic normalisation.  For the first day we can probably normalise the whole data set using say min-max (the data doesn't appear to have a normal distribution)

However, as we progress I think it will be easier to predict percentage changes and that will demand that the first sequence we train on will be movement zero.  This would mean normalising the Y so that we train on percentage changes.

Train, test, validation.

We don't have that much data.  We can increase it by taking sequences in sequences
