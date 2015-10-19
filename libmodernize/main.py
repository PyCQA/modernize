"""\
Python           _              _
   _ __  ___  __| |___ _ _ _ _ (_)______
  | '  \/ _ \/ _` / -_) '_| ' \| |_ / -_)
  |_|_|_\___/\__,_\___|_| |_||_|_/__\___|\
"""

from __future__ import absolute_import, print_function

import io
import sys
import logging
import optparse

from lib2to3.main import warn, StdoutRefactoringTool
from lib2to3 import refactor

from libmodernize import __version__
from libmodernize.fixes import lib2to3_fix_names, six_fix_names, opt_in_fix_names


class LineEndingsRefactoringTool(StdoutRefactoringTool):
    '''2to3 refactoring tool that rewrites files with specified line endings'''
    def __init__(self, *args, newline=None, **kwargs):
        super(LineEndingsRefactoringTool, self).__init__(*args, **kwargs)
        self.newline = newline

    def write_file(self, new_text, filename, old_text, encoding):
        super(LineEndingsRefactoringTool, self).write_file(new_text, filename,
                                                           old_text, encoding)

        if self.newline is not None:
            self.log_debug("Rewriting %s with line endings %r",
                           filename, self.newline)
            with io.open(filename, 'r', encoding=encoding) as f:
                contents = f.read()

            with io.open(filename, 'w', encoding=encoding,
                         newline=self.newline) as f:
                 f.write(contents)


usage = __doc__ + """\
 %s

Usage: modernize [options] file|dir ...
""" % __version__

def format_usage(usage):
    """Method that doesn't output "Usage:" prefix"""
    return usage

def main(args=None):
    """Main program.

    Returns a suggested exit status (0, 1, 2).
    """
    # Set up option parser
    parser = optparse.OptionParser(usage=usage,
                                   version="modernize %s" % __version__)
    parser.formatter.format_usage = format_usage
    parser.add_option("-v", "--verbose", action="store_true",
                      help="Show more verbose logging.")
    parser.add_option("--no-diffs", action="store_true",
                      help="Don't show diffs of the refactoring.")
    parser.add_option("-l", "--list-fixes", action="store_true",
                      help="List available transformations.")
    parser.add_option("-d", "--doctests_only", action="store_true",
                      help="Fix up doctests only.")
    parser.add_option("-f", "--fix", action="append", default=[],
                      help="Each FIX specifies a transformation; '-f default' includes default fixers.")
    parser.add_option("-j", "--processes", action="store", default=1,
                      type="int", help="Run 2to3 concurrently.")
    parser.add_option("-x", "--nofix", action="append", default=[],
                      help="Prevent a fixer from being run.")
    parser.add_option("-p", "--print-function", action="store_true",
                      help="Modify the grammar so that print() is a function.")
    parser.add_option("-w", "--write", action="store_true",
                      help="Write back modified files.")
    parser.add_option("-n", "--nobackups", action="store_true", default=False,
                      help="Don't write backups for modified files.")
    parser.add_option("--six-unicode", action="store_true", default=False,
                      help="Wrap unicode literals in six.u().")
    parser.add_option("--future-unicode", action="store_true", default=False,
                      help="Use 'from __future__ import unicode_literals'"
                      "(only useful for Python 2.6+).")
    parser.add_option("--no-six", action="store_true", default=False,
                      help="Exclude fixes that depend on the six package.")
    parser.add_option("--unix-line-endings", action="store_true", default=False,
                      help="Write files with Unix (LF) line endings.")
    parser.add_option("--windows-line-endings", action="store_true", default=False,
                      help="Write files with Windows (CRLF) line endings.")

    fixer_pkg = 'libmodernize.fixes'
    avail_fixes = set(refactor.get_fixers_from_package(fixer_pkg))
    avail_fixes.update(lib2to3_fix_names)

    # Parse command line arguments
    refactor_stdin = False
    flags = {}
    options, args = parser.parse_args(args)
    if not options.write and options.no_diffs:
        warn("Not writing files and not printing diffs; that's not very useful.")
    if not options.write and options.nobackups:
        parser.error("Can't use '-n' without '-w'.")
    if options.list_fixes:
        print("Available transformations for the -f/--fix option:")
        for fixname in sorted(avail_fixes):
            print(fixname)
        if not args:
            return 0
    if options.unix_line_endings and options.windows_line_endings:
        print("--unix-line-endings and --windows-line-endings are mutually exclusive",
              file=sys.stderr)
        return 2
    if not args:
        print("At least one file or directory argument required.", file=sys.stderr)
        print("Use --help to show usage.", file=sys.stderr)
        return 2
    if "-" in args:
        refactor_stdin = True
        if options.write:
            print("Can't write to stdin.", file=sys.stderr)
            return 2
    if options.print_function:
        flags["print_function"] = True

    # Set up logging handler
    level = logging.DEBUG if options.verbose else logging.INFO
    logging.basicConfig(format='%(name)s: %(message)s', level=level)

    # Initialize the refactoring tool
    unwanted_fixes = set(options.nofix)
    default_fixes = avail_fixes.difference(opt_in_fix_names)

    # Remove unicode fixers depending on command line options
    if options.six_unicode:
        unwanted_fixes.add('libmodernize.fixes.fix_unicode_future')
    elif options.future_unicode:
        unwanted_fixes.add('libmodernize.fixes.fix_unicode')
    else:
        unwanted_fixes.add('libmodernize.fixes.fix_unicode')
        unwanted_fixes.add('libmodernize.fixes.fix_unicode_future')

    if options.no_six:
        unwanted_fixes.update(six_fix_names)
    explicit = set()
    if options.fix:
        default_present = False
        for fix in options.fix:
            if fix == "default":
                default_present = True
            else:
                explicit.add(fix)
        requested = default_fixes.union(explicit) if default_present else explicit
    else:
        requested = default_fixes
    fixer_names = requested.difference(unwanted_fixes)

    if options.unix_line_endings:
        newline = '\n'
    elif options.windows_line_endings:
        newline = '\r\n'
    else:
        newline = None

    rt = LineEndingsRefactoringTool(sorted(fixer_names), flags, sorted(explicit),
                               options.nobackups, not options.no_diffs,
                               newline=newline)

    # Refactor all files and directories passed as arguments
    if not rt.errors:
        if refactor_stdin:
            rt.refactor_stdin()
        else:
            try:
                rt.refactor(args, options.write, options.doctests_only,
                            options.processes)
            except refactor.MultiprocessingUnsupported: # pragma: no cover
                assert options.processes > 1
                print("Sorry, -j isn't supported on this platform.",
                      file=sys.stderr)
                return 1
        rt.summarize()

    # Return error status (0 if rt.errors is zero)
    return int(bool(rt.errors))
