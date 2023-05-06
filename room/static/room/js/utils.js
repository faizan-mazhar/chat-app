function createMessageElement(message, userId, currentUserId) {
    /*
        This function creates a new HTML element to represent message.

        return: HTML element
    */
    let $containerDiv = $("<div>", {"class": "d-flex flex-row mb-4"});

    // text wrapper div
    let $wrapperDiv = $("<div>", {"class": "p-3 me-3 border"});
    $containerDiv.append($wrapperDiv);

    // text element to show message
    let $textNode = $("<p>", {"class": "small mb-0"});
    $textNode.text(message);
    $wrapperDiv.append($textNode);
    
    // Assign correct CSS classes
    if(userId === currentUserId) {
        $containerDiv.addClass("justify-content-start");
        $wrapperDiv.addClass("my-message");
    } else {
        $containerDiv.addClass("justify-content-end");
        $wrapperDiv.addClass("other-message");
    }
    return $containerDiv;
}
