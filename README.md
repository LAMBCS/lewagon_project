# lewagon_project

This is a project to predict the EUR interest rate yield curve for the next 30 days based on previous yield curves.

The choice of 30 days is made to ensure that the prdeiction will go wildly wrong and that we should have significant differences in the metrics ensuring that we can compare how well the model behaves compared to the naive prediction which in this cae would be the current yield curve.

It imagines a world where an individual can only invest in government bonds, FTSE 100 stocks and gold.

The additional knowlege is the current, and previous, base rates and the last, and previously, published inflation rate.

The project is not really about forecasting the yield curve.  If we manage it in any meanigful sense we can all retire.

What the project is designed to do is cover as much of the syllabus as possible.

It is structured around developing a series of models of increasing complexity until we run out of time and then moving on with what we have to delivery.

I imagine the model trajectory to go something like:

1.  Simple regression model.
2.
