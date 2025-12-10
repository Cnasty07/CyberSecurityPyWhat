
from src.wrappers.what_wrapper import pyWhatWrapper # for old main run

from src.wrapper_interface import pyWhatInterface # for new interface run

# Runs new interface
def run_interface():
    wrapper = pyWhatInterface(match_level=2)
    return wrapper.identify("0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97")

# Runs old what.main conversion
def run(**kwargs):
    print("This is a simple run function: ", kwargs['Option'])
    what_wrapper_instance = pyWhatWrapper(distribution=None, option_template=kwargs['Option'])
    result = what_wrapper_instance.json_results(text_input=kwargs['text_input'])
    return result
    
def main():
    interface_results = run_interface()
    print(interface_results)

if __name__ == "__main__":
    main()
