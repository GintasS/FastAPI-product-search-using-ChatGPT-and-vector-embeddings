enum MessageCategory {
  QuestionAboutProductDescription 
  QuestionAboutProductPrice
  Other
}

function ExtractMessageCategoryFromMessage(message: string) -> MessageCategory {
  client GPT4oMini
  prompt #"
    Determine the category of the user's message from the following content:
    {{ message }}

    {{ ctx.output_format }}
  "#
}

test test_message_product_description {
  functions [ExtractMessageCategoryFromMessage]
  args {
    message "What shower gels you have that smell like rabbit"
  }
}

test test_message_product_price {
  functions [ExtractMessageCategoryFromMessage]
  args {
    message "What shower gels you have that cost from 10 to 20 dollars"
  }
}