library(shiny)
library(tidyverse)
library(bslib)
library(gridExtra)

mnist <- read.csv("~/100-sp24/Mini_Projects/MP03/data/mnist.csv")

ui <- page_sidebar(
  theme = bs_theme(version = 5, bootswatch = "morph"),
  title = "PSTAT 100, MP03",
  sidebar = sidebar(h6("Perform dimension reduction on an MNIST image, reconstitute
dimension-reduced image."),
                    sliderInput("dim", label = "Number of dimensions:", min = 1, max = 28,
                                value = 2),
                    helpText("This slider controls the number of dimensions we first
project the image onto. Fewer dimensions result in 'granier' images."),
                    numericInput("rows", label = "Which Row?", min = 0, max = 1000, value
                                 = 1),
                    helpText("This input controls which row (of the thousand rows
included) to use when generating the image.")
  ),
  layout_columns(card(card_header("Reconstituated Image"), plotOutput("distPlot")),
                 card(card_header("True Classification"),textOutput("verb"))
  )
)

server <- function(input, output) {
  output$verb <- renderText({ paste0("The number displayed is ",
                                     mnist[input$rows,1])
  })
  
  output$distPlot <- renderPlot({
    image_gen_ggplot <- function(x) {
      vect <- (x[-1] %>% as.numeric) / 255
      as.im <- matrix(vect,
                      nrow = 28,
                      byrow = T)
      as.im <- scale(as.im, scale = F)
      as.im[nrow(as.im):1,] %>%
        as.data.frame() %>%
        rowid_to_column(var = 'y') %>%
        pivot_longer(
          -y,
          names_to = 'x',
          values_to = "brightness"
        ) %>%
        mutate(x = parse_number(x)) %>%
        ggplot(aes(x = x, y = y, fill = brightness)) +
        geom_raster() +
        theme_void() +
        scale_fill_gradient2(low="white", high="black", guide="none") +
        theme(
          panel.border = element_rect(linewidth = 1,
                                      fill = NA)
        )
    }
    X <- matrix(as.numeric(mnist[input$rows,][-1]),
                nrow = 28,
                byrow = T)
    X_2 <- prcomp(X)$x[,1:input$dim] %*% t(prcomp(X)$rotation[,1:input$dim])
    c(0, as.vector(t(X_2))) %>% image_gen_ggplot()
  })
}

# Run the application
shinyApp(ui = ui, server = server)


