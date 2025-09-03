Project Overview
Our project, AgriSmart, is a smart agricultural agent designed to revolutionize farming in Yemen using artificial intelligence. We have built a practical and sustainable solution that helps farmers make better decisions about their crops based on accurate climate data. This project is not just a technical tool; it's a social and environmental initiative aimed at achieving a more sustainable future.

Our Inspiration
The primary inspiration for our project came from the significant challenges faced by Yemeni farmers. We observed that Qat cultivation consumes a massive amount of groundwater and negatively impacts soil quality, threatening the country's natural resources and agricultural future. Our goal was to use technology to provide a tangible solution to help farmers transition to more profitable crops that are also more suitable for the environment, thereby contributing to reducing Qat cultivation.

What We Learned
The Power of AI in Solving Real-World Problems: We learned that powerful language models like the Gemini AI can analyze complex datasets and provide practical and detailed insights. This shows that AI is not just a recreational tool; it's a partner in solving global problems.

The Importance of Data Quality: We realized that the accuracy of the output heavily depends on the quality of the input data. Therefore, cleaning the raw data from NASA POWER was a crucial step.

Prompt Engineering: The biggest challenge was how to guide the model to get the exact desired output. We learned that crafting a precise prompt is an art in itself.

How We Built It
Data Collection: We started by gathering historical climate data (such as temperature and rainfall) from NASA POWER.

Initial Data Analysis: We used pandas in Python to clean the raw data from its raw CSV format into a structured table.

AI Integration: We built a simple Python script that sends the data to the Gemini API with a detailed Prompt.

The Output: The model provided smart agricultural recommendations about suitable crops (vegetables, fruits, and wheat) that save water and increase income, proving our prototype works.

!(https://example.com/agri_smart_flow.png)

Challenges We Faced
First Challenge: We initially faced errors connecting to the API.

Solution: We discovered the problem was an invalid API key and exceeding the free usage quota. We corrected the key and reduced the data size to fix it.

Second Challenge: The initial results from the model were not very precise.

Solution: We refined the prompt to be more specific, including concepts like sustainability, increased income, and replacing Qat, which led to much better results.

Conclusion: Our project demonstrates that combining climate data with the power of AI can provide an effective solution to agricultural problems in arid regions. This is just the beginning, and we are excited about the future.

For engineering calculations:
\( \Delta P = \rho g h \)
For larger equations:

E=mc 
2
