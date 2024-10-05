class ExtractedProductInformation {
  description string
  price_range string[]
}

function ExtractProductDescriptionAndPriceFromMessage(message: string) -> ExtractedProductInformation {
  client GPT4oMini
  prompt #"
    The user will ask about similar products or product recommendatons in his message. Please extract these from the User's message:
    - product description (if it is present, interpret it as a search query for products, this query might have additional words that describe the product, such as vendor, product type, tags, also any information that could help us identify the product,
      if it's not, return 'No Product Description')
    - product price range (returning it in a list)
      If user only mentioned one price range, return it like this Price < X
      If user mentioned two price ranges, return it like this: first element Price > X, second element Price < Y 
      If user didn't mention any price ranges, or price ranges are invalid, not a numbers, not a valid pandas dataframe mask, return an empty list.

    The message is:
    {{ message }}

    {{ ctx.output_format }}
  "#
}

test test_product_description_with_full_price_range {
  functions [ExtractProductDescriptionAndPriceFromMessage]
  args {
    message "What shower gels you have that smell like rabbit and cost between 10 and 20"
  }
}

test test_product_description_with_one_price_range {
  functions [ExtractProductDescriptionAndPriceFromMessage]
  args {
    message "What shower gels you have that smell like rabbit and cost less than 20"
  }
}

test test_product_description_without_price_range {
  functions [ExtractProductDescriptionAndPriceFromMessage]
  args {
    message "What shower gels you have that smell like rabbit and cost between"
  }
}

test test_product_description_without_price_range2 {
  functions [ExtractProductDescriptionAndPriceFromMessage]
  args {
    message "please find best shampoos you have in the store"
  }
}
