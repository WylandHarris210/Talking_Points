const data = require('./dev.json')[0].trends;


/** Get Twitter Api*/

function getTwitterTrendsResults() {

  const topThreeResults = [];
  for(let i = 0; i < 25; i++) {    [ bob, ,jerry ]
    // Internet Link to Tweetconsole.log("http://twitter.com/search?q=" + data[i].query);
    const currentName = data[i].name;
    if(!currentName.includes('#')){
      topThreeResults[i] = data[i].name;
    }
  }
  return topThreeResults;
}



console.log("All trending topics are:");

/** function that sends twitter trends results to readable csv file */
const fs = require('fs');

function sendTwitterTrendResults(array) {  
  // Define the CSV data rows
  const dataRows = array.map(obj => {
    return Object.values(obj).join('');
  });
  
  // Combine the header and data rows into a single string
  const csvData = dataRows.join(',');
  
  // Write the CSV data to a file
  fs.writeFile('../scrape/topics.csv', csvData, (err) => {
    if (err) throw err;
    console.log('Data written to CSV file successfully');
  });
}


/** API key for ChatGPT API Calls ------------------------ */
const apiKey = '';
const prompt = "'Tell me about '";

// Function that gets answer from prompt
function getAnswerFromOpenAI(apiKey2, prompt2, topResult){
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
    return(responseData);
  }
  generateResponse();
}



//getAnswerFromOpenAI(apiKey, prompt);
let twitterTrendResults = getTwitterTrendsResults();
getAnswerFromOpenAI(apiKey, prompt, twitterTrendResults);
sendTwitterTrendResults(twitterTrendResults);
