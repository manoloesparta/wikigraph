package main

import (
	"fmt"
	"strings"

	"github.com/gocolly/colly"
)

var dir string = "data/"

func main() {
	c := colly.NewCollector(
		colly.MaxDepth(10),
		colly.Async(true),
	)

	c.Limit(&colly.LimitRule{DomainGlob: "*", Parallelism: 5})

	c.OnHTML("a[href]", func(e *colly.HTMLElement) {
		link, end := conditions(e)
		println(e.Text)

		if strings.Contains(link, "/wiki/") && !strings.Contains(end, ":") {
			url := "https://en.wikipedia.org/wiki/" + end
			fmt.Println(url)
			e.Request.Visit(link)
		}
	})

	c.Visit("https://en.wikipedia.org/wiki/Donald_Trump")
	c.Wait()
}

func conditions(e *colly.HTMLElement) (string, string) {
	link := e.Attr("href")
	post := strings.Split(link, "/")
	end := post[len(post)-1]
	return link, end
}

func save(url string) {

}
