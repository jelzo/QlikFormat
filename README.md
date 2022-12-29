# QlikFormat
## Functions
The currently included functions are:
- urlencode
- htmlentities
- linethrough
- underline
- slashtrough
- monospace
- sans_bold
- sans_italic
- sans_bold_italic
- serif
- serif_italic
- serif_bold
- serif_bold_italic
- script
- script_bold

## Usage
```
$(include=[lib://YOUR_LIBRARY/format.qvs]); // Include the script file

// In variables
LET vOutput = $(htmlentities('<html><body>Hello World</body></html>'));

// In (dynamic) load statement
LOAD $(htmlentities([Input])) AS Output;
LOAD '<html><body>Hello World</body></html>' AS Input AUTOGENERATE 1;
```

## Testing
```
LET vURLENCODE = $(urlencode('€5 to $'));
TRACE 'URL Encode: http://www.google.com/search?q=$(vURLENCODE)'; // Prints out url with encoded parameters

LET vHTMLENTITIES = $(htmlentities('<!doctype html><html lang="en"><head></head><body><!-- your content here... --></body></html>'));
TRACE 'HTML Entities: Basic HTML Page <code>$(vHTMLENTITIES)</code>'; // Prints out html with escaped entities
```

## Supported characters
The formatting function converts single characters to the formatted equivalent. For some styling functions (linethrough, underline and slashthrough), it uses a preceeding character. The scope of the function is currently limited to the [Windows-1252 character set](https://nl.wikipedia.org/wiki/Windows-1252) (except the 32 control characters).
