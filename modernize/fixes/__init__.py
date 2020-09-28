from __future__ import generator_stop

fissix_fix_names = {
    "fissix.fixes.fix_apply",
    "fissix.fixes.fix_except",
    "fissix.fixes.fix_exec",
    "fissix.fixes.fix_execfile",
    "fissix.fixes.fix_exitfunc",
    "fissix.fixes.fix_funcattrs",
    "fissix.fixes.fix_has_key",
    "fissix.fixes.fix_idioms",
    "fissix.fixes.fix_long",
    "fissix.fixes.fix_methodattrs",
    "fissix.fixes.fix_ne",
    "fissix.fixes.fix_numliterals",
    "fissix.fixes.fix_operator",
    "fissix.fixes.fix_paren",
    "fissix.fixes.fix_reduce",
    "fissix.fixes.fix_renames",
    "fissix.fixes.fix_repr",
    "fissix.fixes.fix_set_literal",
    "fissix.fixes.fix_standarderror",
    "fissix.fixes.fix_sys_exc",
    "fissix.fixes.fix_throw",
    "fissix.fixes.fix_tuple_params",
    "fissix.fixes.fix_types",
    "fissix.fixes.fix_ws_comma",
    "fissix.fixes.fix_xreadlines",
}

# fixes that involve using six
six_fix_names = {
    "modernize.fixes.fix_basestring",
    "modernize.fixes.fix_dict_six",
    "modernize.fixes.fix_filter",
    "modernize.fixes.fix_imports_six",
    "modernize.fixes.fix_itertools_six",
    "modernize.fixes.fix_itertools_imports_six",
    "modernize.fixes.fix_input_six",
    "modernize.fixes.fix_int_long_tuple",
    "modernize.fixes.fix_map",
    "modernize.fixes.fix_metaclass",
    "modernize.fixes.fix_raise_six",
    "modernize.fixes.fix_unicode",
    "modernize.fixes.fix_unicode_type",
    "modernize.fixes.fix_urllib_six",
    "modernize.fixes.fix_unichr",
    "modernize.fixes.fix_xrange_six",
    "modernize.fixes.fix_zip",
}

# Fixes that are opt-in only.
opt_in_fix_names = {
    "modernize.fixes.fix_classic_division",
    "modernize.fixes.fix_open",
}
