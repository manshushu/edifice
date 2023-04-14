public class ExpandableListActivity extends ExpandableListActivity {

    private HashMap<String, List<String>> mParentItems;
    private ArrayList<String> mHeaders;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_expandable_list);

        // 初始化父项和子项数据源
        initDataSource();

        // 创建Adapter并绑定到ExpandableListView控件上
        final ExpandableListAdapter adapter = new ExpandableListAdapter(this, mHeaders, mParentItems);
        setListAdapter(adapter);

        // 设置ExpandableListView的点击监听器
        getExpandableListView().setOnGroupClickListener(new ExpandableListView.OnGroupClickListener() {
            @Override
            public boolean onGroupClick(ExpandableListView parent, View v, int groupPosition, long id) {
                if (parent.isGroupExpanded(groupPosition)) {
                    parent.collapseGroup(groupPosition);
                } else {
                    parent.expandGroup(groupPosition);
                }
                return true;
            }
        });

        // 设置ExpandableListView子项的点击监听器
        getExpandableListView().setOnChildClickListener(new ExpandableListView.OnChildClickListener() {
            @Override
            public boolean onChildClick(ExpandableListView parent, View v, int groupPosition, int childPosition, long id) {
                Toast.makeText(getApplicationContext(), "你点击了子项：" + adapter.getChild(groupPosition, childPosition), Toast.LENGTH_SHORT).show();
                return false;
            }
        });
    }

    private void initDataSource() {
        // 初始化父项数据源
        mHeaders = new ArrayList<>();
        mHeaders.add("魏国");
        mHeaders.add("蜀国");
        mHeaders.add("吴国");

        // 初始化子项数据源
        mParentItems = new HashMap<>();
        List<String> foodList = new ArrayList<>();
        foodList.add("曹操");
        foodList.add("曹植");
        foodList.add("曹冲");
        mParentItems.put(mHeaders.get(0), foodList);

        List<String> travelList = new ArrayList<>();
        travelList.add("刘备");
        travelList.add("关羽");
        travelList.add("张飞");
        mParentItems.put(mHeaders.get(1), travelList);

        List<String> shoppingList = new ArrayList<>();
        shoppingList.add("周瑜");
        shoppingList.add("吕蒙");
        shoppingList.add("甘宁");
        mParentItems.put(mHeaders.get(2), shoppingList);
    }
}