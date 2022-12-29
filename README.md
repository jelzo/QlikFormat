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

LET output = $(urlencode('input'));
```

## Testing
```
TRACE URL Encode: http://www.google.com/search?q=$(=urlencode('€5 to $')) // Prints out url with encoded parameters
TRACE HTML Entities: Basic HTML Page <code>$(=htmlentities('<!doctype html><html lang="en"><head></head><body><!-- your content here... --></body></html>')) // Prints out html with escaped entities
```

## Supported characters
The formatting function converts single characters to the formatted equivalent. For some styling functions (linethrough, underline and slashthrough), it uses a preceeding character. The function is limited to the [Windows-1252 character set](https://nl.wikipedia.org/wiki/Windows-1252) (except the 32 control characters).
