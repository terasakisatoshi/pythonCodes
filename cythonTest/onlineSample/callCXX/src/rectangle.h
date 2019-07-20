namespace shapes {
    class Rectangle {
    public:
        int x_min,y_min,x_max,y_max;
        Rectangle(int x_min,int y_min,int x_max,int y_max);
        ~Rectangle();
        int getLength();
        int getHeight();
        int getArea();
        void move(int dx,int dy);
    };
}