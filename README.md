# Background
Wikipedia is an accessible online encyclopedia comprising numerous entries covering a wide range of topics. To view a specific entry, one can navigate to its dedicated page, such as https://en.wikipedia.org/wiki/HTML, which displays the Wikipedia entry for HTML. Notably, the requested page's name (HTML) is indicated in the route /wiki/HTML, and the page content is essentially HTML code rendered by the browser.

In practical terms, it would become cumbersome if every Wikipedia page had to be composed in HTML. Therefore, it is more convenient to use a lightweight, user-friendly markup language to store encyclopedia entries. While Wikipedia utilizes Wikitext as its markup language, we will employ Markdown for this project.

To understand Markdown syntax, refer to GitHub's Markdown guide, paying specific attention to formatting elements like headings, bold text, links, and lists. Adopting a one-Markdown-file-per-entry approach enhances the ease of writing and editing entries. However, when a user accesses an encyclopedia entry, we must convert the Markdown content into HTML before presenting it to the user.

# Specification and file distribution
### Entry Page
When accessing /wiki/TITLE, the page should display the contents of the specified encyclopedia entry. To retrieve the content, the view should use the appropriate utility function. If the requested entry doesn't exist, an error page should inform the user. If it does, a page with the entry's content should appear, and the title should include the entry's name.

### Index Page 
Improve index.html to enable users to click on any entry name, redirecting them to the corresponding entry page, rather than just listing all encyclopedia page names.

### Search 
Allow users to input a query into the sidebar's search box to find an encyclopedia entry. If the query matches an entry's name, the user should be redirected to that entry's page. If the query doesn't precisely match an entry's name, the user should be directed to a search results page displaying entries with the query as a substring. For instance, a search query like "ytho" should show Python in the results. Clicking on any entry name in the search results should take the user to that entry's page.

### New Page
Clicking "Create New Page" in the sidebar should lead the user to a page where they can create a new encyclopedia entry. Users can input a title and use a textarea for Markdown content. A button allows them to save the new page. If an entry with the provided title already exists upon saving, an error message appears. Otherwise, the entry is saved, and the user is taken to the new entry's page.

### Edit Page
On each entry page, users can click a link to edit the entry's Markdown content in a pre-filled textarea. A button enables the saving of changes, redirecting the user back to that entry's page after saving.

### Random Page
Clicking "Random Page" in the sidebar transports the user to a randomly selected encyclopedia entry.









