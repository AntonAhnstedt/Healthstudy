class Healthanalyzer:
    """En klass för att analysera hälsodata"""
    
    def __init__(self, df):
        """Initierar Healthanalyzer med en DataFrame"""
        self.df = df
        
    def calc_stats(self):
        """Räknar ut nyckeltal från valda kolumner"""
        columns = ["age",
                   "height",
                   "weight",
                   "systolic_bp",
                   "cholesterol"]
        key_stats = self.df[columns].agg(
            ["mean", "median", "min", "max"])
        return key_stats