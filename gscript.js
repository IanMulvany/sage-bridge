
function lastUpdated(){
  Logger.log("hola");
  // var lastrow = CountColA();
  // Logger.log(lastrow);

  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheets()[1];
  var lastRow = sheet.getLastRow();
  Logger.log(lastRow);

  var range = sheet.getRange(lastRow,1);
  var submitted = range.getValue();
  Logger.log(submitted);
  var range = sheet.getRange(lastRow,2);
  var name = range.getValue();
  Logger.log(name);
  var range = sheet.getRange(lastRow,3);
  var email = range.getValue();
  Logger.log(email);
  var range = sheet.getRange(lastRow,4);
  var interest = range.getValue();
  Logger.log(interest);


  var payload =
      {
        "name": name,
        "email": email,
        "interest": interest,
        "submitted": submitted
      } ;

  return payload ;

}

function CountColA(){
  var sheet = SpreadsheetApp.getActiveSheet();
  var data = sheet.getDataRange().getValues();
  for(var i = data.length-1 ; i >=0 ; i--){
    if (data[i][0] != null && data[i][0] != ''){
      return i+1 ;
    }
  }
}


function testPOST() {
  var url = "https://sage-bridge.herokuapp.com/from_gdocs";

  var payload = lastUpdated();

  var headers = {
    "Authorization" : "Basic " + Utilities.base64Encode("john" + ':' + "asff")
  };

  var params = {
    "method":"POST",
    "Content-Type" : "application/json",
    "payload" : payload,
    "followRedirects" : true,
    "muteHttpExceptions": true,
    "headers":headers
  };

  Logger.log(params);

  var response = UrlFetchApp.fetch(url, params);

  var rc = response.getResponseCode();
  var responseText = response.getContentText();
  if (rc !== 200) {
    // Log HTTP Error
    Logger.log("Response (%s) %s",
               rc,
               responseText );
    // Could throw an exception yourself, if appropriate
  }
  else {
    // Successful POST, handle response normally
    Logger.log( responseText );
  }
}
