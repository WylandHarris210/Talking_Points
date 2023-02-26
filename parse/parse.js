const data = require('./dev.json')[0].trends;

const topThreeResults = [];


for(let i = 0; i < 3; i++) {
  // Internet Link to Tweetconsole.log("http://twitter.com/search?q=" + data[i].query);
  topThreeResults[i] = data[i].name;
}

console.log("All trending topics are:");
console.log(topThreeResults);

const topResult = topThreeResults[1];

const apiKey = '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';
const prompt = "'Tell me about '";

function getAnswerFromOpenAI2(apiKey2, prompt2, topResult){
  const { Configuration, OpenAIApi } = require("openai");

  const configuration = new Configuration({
    apiKey: apiKey2,
  });
  const openai = new OpenAIApi(configuration);

  async function generateResponse() {
    const response = await openai.createCompletion({
      model: "text-ada-001",
      prompt: prompt2 + topResult,
      temperature: 0.7,
      max_tokens: 500,
      top_p: 1,
      frequency_penalty: 0,
      presence_penalty: 0,
    });
    
    const responseData = response.data.choices[0].text;
    console.log(responseData);
  }
  generateResponse();
}


//getAnswerFromOpenAI(apiKey, prompt);
getAnswerFromOpenAI2(apiKey, prompt, topResult);