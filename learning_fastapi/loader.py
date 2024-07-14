import os
import json


class Loader:
    @staticmethod
    def load_zone_mapping():
        with open(os.path.join(os.path.dirname(__file__), 'data', 'zone_mapping.json'), 'r') as f:
            return json.load(f)
        
    @staticmethod
    def load_universe(zone):
        file_path = os.path.join(os.path.dirname(__file__), 'data', 'universe', f'{zone}.json')
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return json.load(f)
        return []
    
    @staticmethod
    def load_returns(date):
        file_path = os.path.join(os.path.dirname(__file__), 'data', 'returns', f'{date}.json')
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return json.load(f)
        return {}
