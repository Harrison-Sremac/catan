import sys
import random
import math
import wx

sys.path.append("./src")
import board

class BoardPanel(wx.Panel):
    def __init__(self, parent):
        super(BoardPanel, self).__init__(parent)
        self.InitBoard()
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def InitBoard(self):
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.hex_radius = 40
        self.board = self.GenerateBoard()

    def GenerateBoard(self):
        biomes = ['Forest', 'Pasture', 'Fields', 'Hills', 'Mountains', 'Desert']
        biome_counts = {'Forest': 4, 'Pasture': 4, 'Fields': 4, 'Hills': 3, 'Mountains': 3, 'Desert': 1}
        
        board = []
        for biome, count in biome_counts.items():
            board.extend([biome] * count)

        board.remove('Desert')  # Remove the desert tile
        random.shuffle(board)
        board.insert(9, 'Desert')  # Insert the desert tile at the center position (index 9)

        return board

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.DrawBoard(dc)

    def DrawBoard(self, dc):
        hex_radius = self.hex_radius
        hex_height = int(hex_radius * 2)
        hex_width = int((3**0.5) * hex_radius)
        # Coordinates for the center of the hex grid
        start_x, start_y = 300, 300

        # Hex grid layout for a standard Catan board
        layout = [
            (-1, -2), (0, -2), (1, -2),
            (-1.5, -1), (-0.5, -1), (0.5, -1), (1.5, -1),
            (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0),
            (-1.5, 1), (-0.5, 1), (0.5, 1), (1.5, 1),
            (-1, 2), (-0, 2), (1, 2)
        ]

        index = 0
        for offset in layout:
            dx, dy = offset
            x = start_x + int(dy * hex_width * 3 / 4)  # swapped dx and dy for rotation
            y = start_y + int(dx * hex_height * 0.866)  # swapped dx and dy for rotation
            
            biome = self.board[index] if index < len(self.board) else 'None'
            self.DrawHexagon(dc, x, y, hex_radius, biome)
            index += 1

    def DrawHexagon(self, dc, x, y, radius, biome):
        points = []
        
        for i in range(6):
            angle = math.pi / 3 * i
            x_i = x + int(radius * math.cos(angle))
            y_i = y + int(radius * math.sin(angle))
            points.append((x_i, y_i))
        
        dc.SetPen(wx.Pen(wx.Colour(0, 0, 0), 2))
        
        biome_colors = {
            'Forest': wx.Colour(34, 139, 34),
            'Pasture': wx.Colour(124, 252, 0),
            'Fields': wx.Colour(255, 215, 0),
            'Hills': wx.Colour(165, 42, 42),
            'Mountains': wx.Colour(169, 169, 169),
            'Desert': wx.Colour(255, 223, 196)
        }
        
        color = biome_colors.get(biome, wx.Colour(255, 255, 255))
        dc.SetBrush(wx.Brush(color))
        dc.DrawPolygon(points)
        
        dc.DrawText(biome, int(x - radius // 2), int(y - 10))

class CatanFrame(wx.Frame):
    """
    Prints the GUI of the Catan game.
    """

    def __init__(self, *args, **kw):
        super(CatanFrame, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.board_panel = BoardPanel(panel)
        sizer.Add(self.board_panel, 1, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(sizer)

        self.SetTitle('Catan Game')
        self.SetSize((800, 600))  # Set the default window size to 800x600

        self.Centre()

def main():
    app = wx.App(False)
    frame = CatanFrame(None)
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
