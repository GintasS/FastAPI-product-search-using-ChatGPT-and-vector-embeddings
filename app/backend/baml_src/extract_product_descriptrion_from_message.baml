class ProductDescription {
  text string
}

function ExtractProductDescriptionFromMessage(message: string) -> ProductDescription {
  client GPT4oMini
  prompt #"
    Extract product description from this user message, without any auxilar verbs, just a product description:
    {{ message }}

    {{ ctx.output_format }}
  "#
}

test test_product_description_extraction_from_message {
  functions [ExtractProductDescriptionFromMessage]
  args {
    message "I want to get a shower gel that has a color blue"
  }
}