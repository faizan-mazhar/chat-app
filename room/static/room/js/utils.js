function createMessageElement(message) {
    /*
        This function creates a new HTML element to represent message.

        return: HTML element
    */
    let $containerDiv = $("<div>", {"class": "d-flex flex-row mb-4"});
    $containerDiv.addClass("justify-content-start");

    // text wrapper div
    let $wrapperDiv = $("<div>", {"class": "p-3 me-3 border"});
    $wrapperDiv.addClass("my-message");
    $containerDiv.append($wrapperDiv);

    // text element to show message
    let $textNode = $("<p>", {"class": "small mb-0"});
    $textNode.text(message);
    $wrapperDiv.append($textNode);
    
    return $containerDiv;
}
