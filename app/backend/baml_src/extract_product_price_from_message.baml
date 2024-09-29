function ExtractProductPriceFromMessage(message: string) -> string[] {
  client GPT4oMini
  prompt #"
    Extract product price from this user message in python dataframe mask format: Price < X".
    If it is a price range, return two masks for the dataframe.
    {{ message }}

    {{ ctx.output_format }}
  "#
}

test test_extract_product_price_extraction_from_message {
  functions [ExtractProductPriceFromMessage]
  args {
    message "I want to get a shower gel below ten dollars"
  }
}

test test_extract_two_product_price_extraction_from_message {
  functions [ExtractProductPriceFromMessage]
  args {
    message "I want to get a shower gel below ten dollars and above 5"
  }
}