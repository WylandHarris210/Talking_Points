const data = require('./dev.json')[0].trends;

/** Parse Twitter Information*/
function getTwitterTrendsResults() {

  let topThreeResults = [];
  let ahhh = 0;

  for(let i = 0; i < 25; i++) { 
    // Internet Link to Tweetconsole.log("http://twitter.com/search?q=" + data[i].query);
    const currentName = data[i].name;
    if(!currentName.includes('#')){
      topThreeResults.push(data[i].name);
      ahhh+=1;
    }
    if(ahhh == 5){
      break;
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
const apiKey = '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';
const prompt = "'Give me a 2 sentence summary of this article: '"; 

// Function that gets answer from prompt
function getAnswerFromOpenAI(apiKey2, prompt2){
  const { Configuration, OpenAIApi } = require("openai");
  const data = require('./outputs.json');
  
  console.log(data.Leicester[0]);


  const configuration = new Configuration({
    apiKey: apiKey2,
  });
  const openai = new OpenAIApi(configuration);

  async function generateResponse() {
    const response = await openai.createCompletion({
      model: "text-ada-001",
      prompt: prompt2 + data,
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
let topThreeResults = getTwitterTrendsResults();

getAnswerFromOpenAI(apiKey, prompt, topThreeResults[0]);
getAnswerFromOpenAI(apiKey, prompt, topThreeResults[1]);
getAnswerFromOpenAI(apiKey, prompt, topThreeResults[2]);

sendTwitterTrendResults(topThreeResults);
