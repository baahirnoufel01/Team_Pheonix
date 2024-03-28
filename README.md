# Team-Pheonix
This is the Screenshot to code converter for Anokha-2024 Hackathon (Round2).

# screenshot-to-code

# Problem statement:

Craft an application that seamlessly translates your design concepts into live front-end code, ensuring a direct correlation between what you envision and the end result.


# Solution:  
This simple app converts a screenshot to code (HTML/Tailwind CSS, or React or Bootstrap or Vue). 

 AI Analysis: To examine the design inputs and extract important data, the program makes use of Intel® AI Analytics Toolkits components including typefaces, color schemes, layout, and interactive features 


Collaboration Tools: With the application's collaboration tools, developers and designers may collaborate easily. Developers can make changes depending on the feedback from designers, who can preview and comment on the generated code in real-time.


Export and Integration: Users can export the created code once they're happy with it in a number of formats that operate with well-known front-end frameworks like Vue.js, Angular, and React. For simple project administration and enhanced development insights, the platform incorporates Intel AI analysis to generate actionable recommendations and optimize code efficiency.

 Performance Optimization: The program makes use of Intel® AI Analytics Toolkits to enhance the output code's performance, guaranteeing quick loads, fluid animations, and economical use of resources

 Continuous Improvement: To increase accuracy and efficiency over time, the AI Design Translator changes its algorithms based on feedback from users. In order to guarantee compatibility with the newest design trends and technology, regular upgrades and enhancements are offered.

#  To run

```bash
cd backend
echo "OPENAI_API_KEY=your_intel_one_api_key_here" > .env
poetry install
poetry shell
poetry run uvicorn main:app --reload --port 7001

```

Run the frontend:

```bash

cd frontend
yarn
yarn dev
```

Open http://localhost:5173 to use the app.

