# pyWhat API Wrapper

## Description

To add a contribution to this project we are creating an extension that is at its core just an api wrapper to convert the command line input into something that can be integrated into pipelines in python.

</br>

## Diagram

```mermaid

```

</br>

## TBD


>    https://github.com/bee-san
>
> Filtration:
>
> --rarity min:max
>
>     Rarity is how unlikely something is to be a false-positive. The higher the number, the more unlikely.
>
>            Only print entries with rarity in range [min,max]. min and max can be omitted.
>
>            Note: PyWhat by default has a rarity of 0.1. To see all matches, with many potential false positives use `0:`.
>
>        --include list
>
>            Only include entries containing at least one tag in a list. List is a comma separated list.
>
>        --exclude list
>
>            Exclude specified tags. List is a comma separated list.
>
>    Sorting:
>
>        --key key_name
>
>            Sort by the given key.
>
>        --reverse
>
>            Sort in reverse order.
>
>        Available keys:
>
>            name - Sort by the name of regex pattern
>
>            rarity - Sort by rarity
>
>            matched - Sort by a matched string
>
>            none - No sorting is done (the default)
>
>    Exporting:
>
>        --json
>
>            Return results in json format.
>
>    Boundaryless mode:
>
>        CLI tool matches strings like 'abcdTHM{hello}plze' by default because the boundaryless mode is enabled for regexes with a rarity of 0.1 and higher.
>
>        Since boundaryless mode may produce a lot of false-positive matches, it is possible to disable it, either fully or partially.
>
>        '--disable-boundaryless' flag can be used to fully disable this mode.
>
>        In addition, '-br', '-bi', and '-be' options can be used to tweak which regexes should be in boundaryless mode.
>
>        Refer to the Filtration section for more information.
>
>    Formatting the output:
>
>        --format format_str
>
>            format_str can be equal to:
>
>                pretty - Output data in the table
>
>                json - Output data in json format
>
>                CUSTOM_STRING - Print data in the way you want. For every match CUSTOM_STRING will be printed and '%x' (See below for possible x values) will be substituted with a match value.
>
>                For example:
>
>                    pywhat --format '%m - %n' 'google.com htb{flag}'
>
>                    will print:
>
>                    htb{flag} - HackTheBox Flag Format
>                    google.com - Uniform Resource Locator (URL)
>
>                Possible '%x' values:
>
>                    %m - matched text
>
>                    %n - name of regex
>
>                    %d - description (will not output if absent)
>
>                    %e - exploit (will not output if absent)
>
>                    %r - rarity
>
>                    %l - link (will not output if absent)
>
>                    %t - tags (in 'tag1, tag2 ...' format)
>
>                If you want to print '%' or '\\' character - escape it: '\\%', '\\\\'.
>
>    Examples:
>
>        * what 'HTB{this is a flag}'
>
>        * what '0x52908400098527886E0F7030069857D2E4169EE7'
>
>        * what -- '52.6169586, -1.9779857'
>
>        * what --rarity 0.6: 'myEmail@host.org'
>
>        * what --rarity 0: --include "credentials" --exclude "aws" 'James:SecretPassword'
>
>        * what -br 0.6: -be URL '123myEmail@host.org456'
>
> Your text must either be in quotation marks, or use the POSIX standard of "--" to mean "anything after -- is textual input".
>
>
> pyWhat can also search files or even a whole directory with recursion:
>
> what 'secret.txt'
>
> what 'this/is/a/path'
>