# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_consensus', [dirname(__file__)])
        except ImportError:
            import _consensus
            return _consensus
        if fp is not None:
            try:
                _mod = imp.load_module('_consensus', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _consensus = swig_import_helper()
    del swig_import_helper
else:
    import _consensus
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



_consensus.LIBBITCOIN_CONSENSUS_VERSION_swigconstant(_consensus)
LIBBITCOIN_CONSENSUS_VERSION = _consensus.LIBBITCOIN_CONSENSUS_VERSION

_consensus.LIBBITCOIN_CONSENSUS_MAJOR_VERSION_swigconstant(_consensus)
LIBBITCOIN_CONSENSUS_MAJOR_VERSION = _consensus.LIBBITCOIN_CONSENSUS_MAJOR_VERSION

_consensus.LIBBITCOIN_CONSENSUS_MINOR_VERSION_swigconstant(_consensus)
LIBBITCOIN_CONSENSUS_MINOR_VERSION = _consensus.LIBBITCOIN_CONSENSUS_MINOR_VERSION

_consensus.LIBBITCOIN_CONSENSUS_PATCH_VERSION_swigconstant(_consensus)
LIBBITCOIN_CONSENSUS_PATCH_VERSION = _consensus.LIBBITCOIN_CONSENSUS_PATCH_VERSION

_consensus.verify_result_eval_false_swigconstant(_consensus)
verify_result_eval_false = _consensus.verify_result_eval_false

_consensus.verify_result_eval_true_swigconstant(_consensus)
verify_result_eval_true = _consensus.verify_result_eval_true

_consensus.verify_result_script_size_swigconstant(_consensus)
verify_result_script_size = _consensus.verify_result_script_size

_consensus.verify_result_push_size_swigconstant(_consensus)
verify_result_push_size = _consensus.verify_result_push_size

_consensus.verify_result_op_count_swigconstant(_consensus)
verify_result_op_count = _consensus.verify_result_op_count

_consensus.verify_result_stack_size_swigconstant(_consensus)
verify_result_stack_size = _consensus.verify_result_stack_size

_consensus.verify_result_sig_count_swigconstant(_consensus)
verify_result_sig_count = _consensus.verify_result_sig_count

_consensus.verify_result_pubkey_count_swigconstant(_consensus)
verify_result_pubkey_count = _consensus.verify_result_pubkey_count

_consensus.verify_result_verify_swigconstant(_consensus)
verify_result_verify = _consensus.verify_result_verify

_consensus.verify_result_equalverify_swigconstant(_consensus)
verify_result_equalverify = _consensus.verify_result_equalverify

_consensus.verify_result_checkmultisigverify_swigconstant(_consensus)
verify_result_checkmultisigverify = _consensus.verify_result_checkmultisigverify

_consensus.verify_result_checksigverify_swigconstant(_consensus)
verify_result_checksigverify = _consensus.verify_result_checksigverify

_consensus.verify_result_numequalverify_swigconstant(_consensus)
verify_result_numequalverify = _consensus.verify_result_numequalverify

_consensus.verify_result_bad_opcode_swigconstant(_consensus)
verify_result_bad_opcode = _consensus.verify_result_bad_opcode

_consensus.verify_result_disabled_opcode_swigconstant(_consensus)
verify_result_disabled_opcode = _consensus.verify_result_disabled_opcode

_consensus.verify_result_invalid_stack_operation_swigconstant(_consensus)
verify_result_invalid_stack_operation = _consensus.verify_result_invalid_stack_operation

_consensus.verify_result_invalid_altstack_operation_swigconstant(_consensus)
verify_result_invalid_altstack_operation = _consensus.verify_result_invalid_altstack_operation

_consensus.verify_result_unbalanced_conditional_swigconstant(_consensus)
verify_result_unbalanced_conditional = _consensus.verify_result_unbalanced_conditional

_consensus.verify_result_sig_hashtype_swigconstant(_consensus)
verify_result_sig_hashtype = _consensus.verify_result_sig_hashtype

_consensus.verify_result_sig_der_swigconstant(_consensus)
verify_result_sig_der = _consensus.verify_result_sig_der

_consensus.verify_result_minimaldata_swigconstant(_consensus)
verify_result_minimaldata = _consensus.verify_result_minimaldata

_consensus.verify_result_sig_pushonly_swigconstant(_consensus)
verify_result_sig_pushonly = _consensus.verify_result_sig_pushonly

_consensus.verify_result_sig_high_s_swigconstant(_consensus)
verify_result_sig_high_s = _consensus.verify_result_sig_high_s

_consensus.verify_result_sig_nulldummy_swigconstant(_consensus)
verify_result_sig_nulldummy = _consensus.verify_result_sig_nulldummy

_consensus.verify_result_pubkeytype_swigconstant(_consensus)
verify_result_pubkeytype = _consensus.verify_result_pubkeytype

_consensus.verify_result_cleanstack_swigconstant(_consensus)
verify_result_cleanstack = _consensus.verify_result_cleanstack

_consensus.verify_result_minimalif_swigconstant(_consensus)
verify_result_minimalif = _consensus.verify_result_minimalif

_consensus.verify_result_sig_nullfail_swigconstant(_consensus)
verify_result_sig_nullfail = _consensus.verify_result_sig_nullfail

_consensus.verify_result_discourage_upgradable_nops_swigconstant(_consensus)
verify_result_discourage_upgradable_nops = _consensus.verify_result_discourage_upgradable_nops

_consensus.verify_result_discourage_upgradable_witness_program_swigconstant(_consensus)
verify_result_discourage_upgradable_witness_program = _consensus.verify_result_discourage_upgradable_witness_program

_consensus.verify_result_op_return_swigconstant(_consensus)
verify_result_op_return = _consensus.verify_result_op_return

_consensus.verify_result_unknown_error_swigconstant(_consensus)
verify_result_unknown_error = _consensus.verify_result_unknown_error

_consensus.verify_result_witness_program_wrong_length_swigconstant(_consensus)
verify_result_witness_program_wrong_length = _consensus.verify_result_witness_program_wrong_length

_consensus.verify_result_witness_program_empty_witness_swigconstant(_consensus)
verify_result_witness_program_empty_witness = _consensus.verify_result_witness_program_empty_witness

_consensus.verify_result_witness_program_mismatch_swigconstant(_consensus)
verify_result_witness_program_mismatch = _consensus.verify_result_witness_program_mismatch

_consensus.verify_result_witness_malleated_swigconstant(_consensus)
verify_result_witness_malleated = _consensus.verify_result_witness_malleated

_consensus.verify_result_witness_malleated_p2sh_swigconstant(_consensus)
verify_result_witness_malleated_p2sh = _consensus.verify_result_witness_malleated_p2sh

_consensus.verify_result_witness_unexpected_swigconstant(_consensus)
verify_result_witness_unexpected = _consensus.verify_result_witness_unexpected

_consensus.verify_result_witness_pubkeytype_swigconstant(_consensus)
verify_result_witness_pubkeytype = _consensus.verify_result_witness_pubkeytype

_consensus.verify_result_tx_invalid_swigconstant(_consensus)
verify_result_tx_invalid = _consensus.verify_result_tx_invalid

_consensus.verify_result_tx_size_invalid_swigconstant(_consensus)
verify_result_tx_size_invalid = _consensus.verify_result_tx_size_invalid

_consensus.verify_result_tx_input_invalid_swigconstant(_consensus)
verify_result_tx_input_invalid = _consensus.verify_result_tx_input_invalid

_consensus.verify_result_negative_locktime_swigconstant(_consensus)
verify_result_negative_locktime = _consensus.verify_result_negative_locktime

_consensus.verify_result_unsatisfied_locktime_swigconstant(_consensus)
verify_result_unsatisfied_locktime = _consensus.verify_result_unsatisfied_locktime

_consensus.verify_flags_none_swigconstant(_consensus)
verify_flags_none = _consensus.verify_flags_none

_consensus.verify_flags_p2sh_swigconstant(_consensus)
verify_flags_p2sh = _consensus.verify_flags_p2sh

_consensus.verify_flags_strictenc_swigconstant(_consensus)
verify_flags_strictenc = _consensus.verify_flags_strictenc

_consensus.verify_flags_dersig_swigconstant(_consensus)
verify_flags_dersig = _consensus.verify_flags_dersig

_consensus.verify_flags_low_s_swigconstant(_consensus)
verify_flags_low_s = _consensus.verify_flags_low_s

_consensus.verify_flags_nulldummy_swigconstant(_consensus)
verify_flags_nulldummy = _consensus.verify_flags_nulldummy

_consensus.verify_flags_sigpushonly_swigconstant(_consensus)
verify_flags_sigpushonly = _consensus.verify_flags_sigpushonly

_consensus.verify_flags_minimaldata_swigconstant(_consensus)
verify_flags_minimaldata = _consensus.verify_flags_minimaldata

_consensus.verify_flags_discourage_upgradable_nops_swigconstant(_consensus)
verify_flags_discourage_upgradable_nops = _consensus.verify_flags_discourage_upgradable_nops

_consensus.verify_flags_cleanstack_swigconstant(_consensus)
verify_flags_cleanstack = _consensus.verify_flags_cleanstack

_consensus.verify_flags_checklocktimeverify_swigconstant(_consensus)
verify_flags_checklocktimeverify = _consensus.verify_flags_checklocktimeverify

_consensus.verify_flags_checksequenceverify_swigconstant(_consensus)
verify_flags_checksequenceverify = _consensus.verify_flags_checksequenceverify

_consensus.verify_flags_witness_swigconstant(_consensus)
verify_flags_witness = _consensus.verify_flags_witness

_consensus.verify_flags_discourage_upgradable_witness_program_swigconstant(_consensus)
verify_flags_discourage_upgradable_witness_program = _consensus.verify_flags_discourage_upgradable_witness_program

_consensus.verify_flags_minimal_if_swigconstant(_consensus)
verify_flags_minimal_if = _consensus.verify_flags_minimal_if

_consensus.verify_flags_null_fail_swigconstant(_consensus)
verify_flags_null_fail = _consensus.verify_flags_null_fail

_consensus.verify_flags_witness_public_key_compressed_swigconstant(_consensus)
verify_flags_witness_public_key_compressed = _consensus.verify_flags_witness_public_key_compressed

def verify_script(transaction, transaction_size, prevout_script, prevout_script_size, prevout_value, tx_input_index, flags):
    return _consensus.verify_script(transaction, transaction_size, prevout_script, prevout_script_size, prevout_value, tx_input_index, flags)
verify_script = _consensus.verify_script
# This file is compatible with both classic and new-style classes.


