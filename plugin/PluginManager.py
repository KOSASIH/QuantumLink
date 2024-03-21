import os
import importlib.util

class PluginManager:
    def __init__(self):
        self.plugins = {}

    def load_plugins(self, directory):
        """
        Load plugins from the specified directory.
        """
        for file in os.listdir(directory):
            if file.endswith(".py"):
                plugin_path = os.path.join(directory, file)
                plugin_name = os.path.splitext(file)[0]
                spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
                plugin_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(plugin_module)
                self.plugins[plugin_name] = plugin_module

    def run_plugin(self, plugin_name, *args, **kwargs):
        """
        Run a plugin with the specified name.
        """
        if plugin_name in self.plugins:
            plugin = self.plugins[plugin_name]
            plugin.run(*args, **kwargs)
        else:
            print(f"Plugin '{plugin_name}' not found.")

# Example plugin usage
if __name__ == "__main__":
    plugin_manager = PluginManager()
    plugin_manager.load_plugins("plugins/")
    plugin_manager.run_plugin("example_plugin", param1=10, param2="hello")
