package main

import (
	"strings"

	"github.com/gocolly/colly"
)

func main() {
	c := colly.NewCollector(
		colly.MaxDepth(10),
		colly.Async(true),
	)

	c.Limit(&colly.LimitRule{DomainGlob: "*", Parallelism: 10})

	c.OnHTML("a[href]", func(e *colly.HTMLElement) {
		link := e.Attr("href")
		post := strings.Split(link, "/")
		end := post[len(post)-1]
		if strings.Contains(link, "/wiki/") && !strings.Contains(end, ":") {
			println("https://en.wikipedia.org/wiki/" + end)
			e.Request.Visit(link)
		}
	})

	c.Visit("https://en.wikipedia.org/wiki/Donald_Trump")
	c.Wait()
}
