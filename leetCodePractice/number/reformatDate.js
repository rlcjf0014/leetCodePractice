/**
 * @param {string} date
 * @return {string}
 */
 var reformatDate = function(date) {
    const monthInfo = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", 
                       "Aug", "Sep", "Oct","Nov","Dec"];
    const arrayDate = date.split(" ");
    const resultArr = arrayDate.map((element, index) => {
        if (index === 0) {
            if (element.length === 4) {
                return element[0] + element[1];
            } else {
                return "0" + element[0];
            }
        } else if (index === 1) {
            const monthDate = monthInfo.indexOf(element) + 1;
            return String(monthDate).length === 1 ? "0"+monthDate : String(monthDate);
        } else {
            return element;
        }    
    })
    let result = "";
    for (let i= resultArr.length - 1; i >=0; i--) {
        if (i === 0) {
            result += resultArr[i];
        } else {
            result = result + resultArr[i] + "-"
        }
    }
    return result;    
    
};